"""MRF24J40 driver for Micro Python"""

import pyb

import mrf24j40consts

class MRF24J40:
    def __init__(self, spi, cs, ce, channel=46, payload_size=16):
        assert payload_size <= 32

        # init the SPI bus and pins
        spi.init(1, spi.MASTER, baudrate=4000000, polarity=0, phase=0, firstbit=spi.MSB)
        cs.init(cs.OUT_PP, cs.PULL_NONE)
        ce.init(ce.OUT_PP, ce.PULL_NONE)

        # store the pins
        self.spi = spi
        self.cs = cs
        self.ce = ce

        # reset everything
        self.ce.low()
        self.cs.high()
        #self.payload_size = payload_size
        #self.pipe0_read_addr = None
        pyb.delay(5)

        # initialize the MRF24J40 according to Example 3-1 of the datasheet
        self.reset_sw()
        self.reg_short_write(self, PACON2, 0x98) # TODO: replace with symbolic names
        self.reg_short_write(self, TXSTBL, 0x95)
        self.reg_long_write(self, RFCON0, 0x03)
        self.reg_long_write(self, RFCON1, 0x01)
        self.reg_long_write(self, RFCON2, 0x80)
        self.reg_long_write(self, RFCON6, 0x90)
        self.reg_long_write(self, RFCON7, 0x80)
        self.reg_long_write(self, RFCON8, 0x10)
        self.reg_long_write(self, SLPCON1, 0x21)

        self.reg_short_write(self, BBREG2, 0x80)
        self.reg_short_write(self, CCAEDTH, 0x60)
        self.reg_short_write(self, BBREG6, 0x40)

        #enable interrupts
        pyb.enable_irq()

        val = self.reg_short_read(INTCON)
        val &= ~(0x1|0x8) #Clear TXNIE and RXIE. Enable interrupts
        self.reg_short_write(INTCON, val)
        
        # set channel
        self.set_channel(CHANNEL_26)

        # set transmission power
        self.reg_long_write(self, RFCON3, 0x0) # 0dBm

        self.reset_radio()
        ## done?

    def reg_short_read(self, reg):
        self.cs.low()
        self.spi.send(reg<<1)
        buf = self.spi.recv(1)
        self.cs.high()
        return buf[0]

    def reg_long_read(self, reg):
        self.cs.low()
        self.spi.send(0x80 | reg>>3)
        self.spi.send((reg & 0x7)<<5)
        buf = self.spi.recv(1)
        self.cs.high()
        return buf[0]

    def reg_short_write(self, reg, buf):
        self.cs.low()
        self.spi.send(reg<<1 | 0x1)
        self.spi.send(buf)
        self.cs.high()
        return status

    def reg_long_write(self, reg, buf):
        self.cs.low()
        self.spi.send(0x80 | reg>>3)
        self.spi.send(((reg & 0x7)<<5) | 0x1)
        self.spi.send(buf)
        self.cs.high()

    def reset_pin(self):
        self.resetpin.low()
        pyb.delay(2)
        self.resetpin.high()
        pyb.delay(2)

    def reset_sw(self):
        self.reg_short_write(SOFTRST, RSTPWR | RSTBB | RSTMAC)
        pyb.delay(2)

    def reset_radio(self):
        self.reg_short_write(RFCTL, RFRST)
        pyb.delay(2)
        self.reg_short_write(RFCTL, 0)
        pyb.delay(2)
        
    def set_channel(self, channel):
        assert channel >= CHANNEL_11 and channel <= CHANNEL_26 and (channel & 0x0f) == 0x3)
        self.reg_long_write(RFCON0, channel)

    def recv(self):
        irqstate = pyb.disable_irq()

        # Set RXDECINV = 1; disable receiving packets off air.
        self.reg_short_write(BBREG1, RXDECINV)
        
        # Read address, 0x300; get RXFIFO frame length value.
        len = self.reg_short_read(RX)

        # Read RXFIFO addresses, 0x301 through (0x300 + Frame Length + 2); read packet data plus LQI and RSSI.
        buf = []
        for i in range(len):
            buf[i] = self.reg_short_read(RX+1+i)

        lqi = self.reg_short_read(RX_FIFO+len+1)
        rssi = self.reg_short_read(RX_FIFO+len+2)
        
        # Clear RXDECINV = 0; enable receiving packets.
        self.reg_short_write(BBREG1, 0)

        pyb.enable_irq(irqstate)

        return buf

    def set_pan(pan):
        self.reg_short_write(PANIDH, pan >> 8)
        self.reg_short_write(PANIDL, pan & 0xFF)

    def set_short_address(addr):
        self.reg_short_write(SADRH, addr >> 8)
        self.reg_short_write(SADRL, addr & 0xFF)
    
    def send(self, buf, hdr_len, frame_len, timeout=500):
        # Request ACK
        txn = self.reg_short_read(TXNCON)
        self.reg_short_write(TXNCON, txn | TXNACKREQ)
        
        self.reg_long_write(TX_FIFO, hdr_len)
        self.reg_long_write(TX_FIFO+1, frame_len)

        for i in range(frame_len):
            self.reg_long_write(TX_FIFO+2+i, buf[i])

        #TODO: encryption, etc
        self.reg_short_write(TXNCON, txn | TXNTRIG)
        
        
        
        # power up
        self.reg_write(CONFIG, (self.reg_read(CONFIG) | PWR_UP) & ~PRIM_RX)
        pyb.udelay(150)

        # send the data
        self.cs.low()
        self.spi.send(W_TX_PAYLOAD)
        self.spi.send(buf)
        if len(buf) < self.payload_size:
            self.spi.send(b'\x00' * (self.payload_size - len(buf))) # pad out data
        self.cs.high()

        # enable the chip so it can send the data
        self.ce.high()
        pyb.udelay(15) # needs to be >10us
        self.ce.low()

        # blocking wait for tx complete
        start = pyb.millis()
        while pyb.millis() - start < timeout:
            status = self.reg_read_ret_status(OBSERVE_TX)
            if status & (TX_DS | MAX_RT):
                break

        # get and clear all status flags
        status = self.reg_write(STATUS, RX_DR | TX_DS | MAX_RT)
        if not (status & TX_DS):
            raise OSError("send failed")

        # power down
        self.reg_write(CONFIG, self.reg_read(CONFIG) & ~PWR_UP)

                    
