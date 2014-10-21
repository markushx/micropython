"""MRF24J40 driver for Micro Python

import mrf24j40
from pyb import SPI, Pin

def int_handler(line):
    ret = mrf.int_tasks()
    if ((ret & MRF24J40_INT_RX) != 0):
        mrf.recv()
    if ((ret & MRF24J40_INT_TX) != 0):
        print ("TX done")

spi = SPI(1, SPI.MASTER, baudrate=400000, polarity=0, phase=1, firstbit=SPI.MSB)
pin_cs    = Pin(Pin.board.X5,  Pin.OUT_PP)
pin_wake  = Pin(Pin.board.Y11, Pin.OUT_PP)
pin_reset = Pin(Pin.board.Y12, Pin.OUT_PP)
mrf = mrf24j40.MRF24J40(spi, pin_cs, pin_wake, pin_reset, interrupt='Y10', ihandler=int_handler)

mrf.set_pan(0xcafe)
mrf.reg_short_read(mrf24j40.PANIDH)
"""

import pyb

MRF24J40_INT_RX = const(0x1)
MRF24J40_INT_TX = const(0x2)

"""Constants for the MRF24J40 driver for Micro Python"""

# MRF24J40 short registers
RXMCR      = const(0x00)
PANIDL     = const(0x01)
PANIDH     = const(0x02)
SADRL      = const(0x03)
SADRH      = const(0x04)
EADR0      = const(0x05)
EADR1      = const(0x06)
EADR2      = const(0x07)
EADR3      = const(0x08)
EADR4      = const(0x09)
EADR5      = const(0x0A)
EADR6      = const(0x0B)
EADR7      = const(0x0C)
RXFLUSH    = const(0x0D)
#RESERVED  = const(0x0E)
#RESERVED  = const(0x0F)

ORDER     = const(0x10)
TXMCR     = const(0x11)
ACKTMOUT  = const(0x12)
ESLOTG1   = const(0x13)
SYMTICKL  = const(0x14)
SYMTICKH  = const(0x15)
PACON0    = const(0x16)
PACON1    = const(0x17)
PACON2    = const(0x18)
#RESERVED = const(0x19)
TXBCON0   = const(0x1A)
TXNCON    = const(0x1B)
TXG1CON   = const(0x1C)
TXG2CON   = const(0x1D)
ESLOTG23  = const(0x1E)
ESLOTG45  = const(0x1F)

ESLOTG67  = const(0x20)
TXPEND    = const(0x21)
WAKECON   = const(0x22)
FRMOFFSET = const(0x23)
TXSTAT    = const(0x24)
TXBCON1   = const(0x25)
GATECLK   = const(0x26)
TXTIME    = const(0x27)
HSYMTMRL  = const(0x28)
HSYMTMRH  = const(0x29)
SOFTRST   = const(0x2A)
#RESERVED = const(0x2B)
SECCON0   = const(0x2C)
SECCON1   = const(0x2D)
TXSTBL    = const(0x2E)
#RESERVED = const(0x2F)

RXSR      = const(0x30)
INTSTAT   = const(0x31)
INTCON    = const(0x32)
GPIO      = const(0x33)
TRISGPIO  = const(0x34)
SLPACK    = const(0x35)
RFCTL     = const(0x36)
SECCR2    = const(0x37)
BBREG0    = const(0x38)
BBREG1    = const(0x39)
BBREG2    = const(0x3A)
BBREG3    = const(0x3B)
BBREG4    = const(0x3C)
#RESERVED = const(0x3D)
BBREG6    = const(0x3E)
CCAEDTH   = const(0x3F)

#TODO: long
RFCON0    = const(0x200)
RFCON1    = const(0x201)
RFCON2    = const(0x202)
RFCON3    = const(0x203)
#RESERVED = const(0x204)
RFCON5    = const(0x205)
RFCON6    = const(0x206)
RFCON7    = const(0x207)
RFCON8    = const(0x208)
SLPCAL0   = const(0x209)
SLPCAL1   = const(0x20A)
SLPCAL2   = const(0x20B)
#RESERVED = const(0x20C)
#RESERVED = const(0x20D)
#RESERVED = const(0x20E)
RFSTATE   = const(0x20F)

RSSI      = const(0x210)
SLPCON0   = const(0x211)
#RESERVED = const(0x212)
#RESERVED = const(0x213)
#RESERVED = const(0x214)
#RESERVED = const(0x215)
#RESERVED = const(0x216)
#RESERVED = const(0x217)
#RESERVED = const(0x218)
#RESERVED = const(0x219)
#RESERVED = const(0x21A)
#RESERVED = const(0x21B)
#RESERVED = const(0x21C)
#RESERVED = const(0x21D)
#RESERVED = const(0x21F)

SLPCON1   = const(0x220)
#RESERVED = const(0x221)
WAKETIMEL = const(0x222)
WAKETIMEH = const(0x223)
REMCNTL   = const(0x224)
REMCNTH   = const(0x225)
MAINCNT0  = const(0x226)
MAINCNT1  = const(0x227)
MAINCNT2  = const(0x228)
MAINCNT3  = const(0x229)
#RESERVED = const(0x22A)
#RESERVED = const(0x22B)
#RESERVED = const(0x22C)
#RESERVED = const(0x22D)
#RESERVED = const(0x22E)
TESTMODE  = const(0x22F)

ASSOEADR0 = const(0x230)
ASSOEADR1 = const(0x231)
ASSOEADR2 = const(0x232)
ASSOEADR3 = const(0x233)
ASSOEADR4 = const(0x234)
ASSOEADR5 = const(0x235)
ASSOEADR6 = const(0x236)
ASSOEADR7 = const(0x237)
ASSOSADR0 = const(0x238)
ASSOSADR1 = const(0x239)
#RESERVED = const(0x23A)
#RESERVED = const(0x23B)
#UNIMPLEM = const(0x23C)
#UNIMPLEM = const(0x23D)
#UNIMPLEM = const(0x23E)
#UNIMPLEM = const(0x23F)

UPNONCE0  = const(0x240)
UPNONCE1  = const(0x241)
UPNONCE2  = const(0x242)
UPNONCE3  = const(0x243)
UPNONCE4  = const(0x244)
UPNONCE5  = const(0x245)
UPNONCE6  = const(0x246)
UPNONCE7  = const(0x247)
UPNONCE8  = const(0x248)
UPNONCE9  = const(0x249)
UPNONCE10 = const(0x24A)
UPNONCE11 = const(0x24B)
UPNONCE12 = const(0x24C)

RX_FIFO = const(0x300)
TX_FIFO = const(0x000)

CHANNEL_11 = const(0x03)
CHANNEL_12 = const(0x13)
CHANNEL_13 = const(0x23)
CHANNEL_14 = const(0x33)
CHANNEL_15 = const(0x43)
CHANNEL_16 = const(0x53)
CHANNEL_17 = const(0x63)
CHANNEL_18 = const(0x73)
CHANNEL_19 = const(0x83)
CHANNEL_20 = const(0x93)
CHANNEL_21 = const(0xA3)
CHANNEL_22 = const(0xB3)
CHANNEL_23 = const(0xC3)
CHANNEL_24 = const(0xD3)
CHANNEL_25 = const(0xE3)
CHANNEL_26 = const(0xF3)

#RXMCR register 0x00
NOACKRSP  = const(0x20)
PANCOORD  = const(0x08)
COORD     = const(0x04)
ERRPKT    = const(0x02)
PROMI     = const(0x01)

#PACON2 register 0x18
FIFOEN    = const(0x80)
TXONTS3   = const(0x20)
TXONTS2   = const(0x10)
TXONTS1   = const(0x08)
TXONTS0   = const(0x04)
TXONT8    = const(0x02)
TXONT7    = const(0x01)

#TXNCON register 0x1B
FPSTAT    = const(0x10)
INDIRECT  = const(0x08)
TXNACKREQ = const(0x04)
TXNSECEN  = const(0x02)
TXNTRIG   = const(0x01)

# SOFTRST register 0x2A
RSTPWR    = const(0x04)
RSTBB     = const(0x02)
RSTMAC    = const(0x01)

#TXSTBL register 0x2E
RFSTBL3  = const(0x80)
RFSTBL2  = const(0x40)
RFSTBL1  = const(0x20)
RFSTBL0  = const(0x10)
MSIFS3   = const(0x08)
MSIFS2   = const(0x04)
MSIFS1   = const(0x02)
MSIFS0   = const(0x01)

#INTSTAT register 0x31
SLPIF     = const(0x80)
WAKEIF    = const(0x40)
HSYMTMRIF = const(0x20)
SECIF     = const(0x10)
RXIF      = const(0x08)
TXG2IF    = const(0x04)
TXG1IF    = const(0x02)
TXNIF     = const(0x01)

# RFCTL register 0x36
WAKECNT8  = const(0x10)
WAKECNT7  = const(0x08)
RFRST     = const(0x04)
RFTXMODE  = const(0x02)
RFRXMODE  = const(0x01)

# BBREG1 register 0x39
RXDECINV  = const(0x04)

# BBREG2 register 0x3A
CCAMODE1  = const(0x80)
CCAMODE0  = const(0x40)
CCACSTH3  = const(0x20)
CCACSTH2  = const(0x10)
CCACSTH1  = const(0x08)
CCACSTH0  = const(0x04)

# BBREG6 register 0x3E
RSSIMODE1 = const(0x80)
RSSIMODE0 = const(0x40)
RSSIRDY   = const(0x01)

# CCAEDTH register 0x3F
CCAEDTH7  = const(0x80)
CCAEDTH6  = const(0x40)
CCAEDTH5  = const(0x20)
CCAEDTH4  = const(0x10)
CCAEDTH3  = const(0x08)
CCAEDTH2  = const(0x04)
CCAEDTH1  = const(0x02)
CCAEDTH0  = const(0x01)

#RFCON0 register 0x200
CHANNEL3  = const(0x80)
CHANNEL2  = const(0x40)
CHANNEL1  = const(0x20)
CHANNEL0  = const(0x10)
RFOPT3    = const(0x08)
RFOPT2    = const(0x04)
RFOPT1    = const(0x02)
RFOPT0    = const(0x01)

#RFCON1 register 0x201
VCOOPT7   = const(0x80)
VCOOPT6   = const(0x40)
VCOOPT5   = const(0x20)
VCOOPT4   = const(0x10)
VCOOPT3   = const(0x08)
VCOOPT2   = const(0x04)
VCOOPT1   = const(0x02)
VCOOPT0   = const(0x01)

#RFCON2 register 0x202
PLLEN     = const(0x80)

#RFCON6 register 0x206
TXFIL     = const(0x80)
20MRECVR  = const(0x10)
BATEN     = const(0x08)

#RFCON7 register 0x207
SLPCLKSEL1 = const(0x80)
SLPCLKSEL2 = const(0x40)

#RFCON8 register 0x208
RFVCO     = const(0x10)

#RFCON1 register 0x220
CLKOUTEN_N = const(0x20)
SLPCLKDIV4 = const(0x10)
SLPCLKDIV3 = const(0x08)
SLPCLKDIV2 = const(0x04)
SLPCLKDIV1 = const(0x02)
SLPCLKDIV0 = const(0x01)

#... TODO more registers

class MRF24J40:
    def __init__(self, spi, cs, wake, reset, interrupt, ihandler, channel=CHANNEL_26):
        # init the SPI bus and pins
        cs.init(cs.OUT_PP, cs.PULL_NONE)
        wake.init(wake.OUT_PP, wake.PULL_NONE)
        reset.init(reset.OUT_PP, reset.PULL_NONE)

        # store the pins
        self.spi = spi
        self.cs = cs
        self.wake = wake #not used yet
        self.reset = reset #not used yet
        self.interrupt = interrupt #not used yet
        self.ihandler = ihandler #not used yet
        ext = pyb.ExtInt(interrupt, pyb.ExtInt.IRQ_FALLING,
                         pyb.Pin.PULL_DOWN, ihandler)

        # reset everything
        self.reset.low()
        pyb.delay(1)
        self.reset.high()

        self.cs.high()
        pyb.delay(1)

        # initialize the MRF24J40 according to Example 3-1 of the datasheet
        self.reset_sw()
        self.reg_short_write(PACON2, FIFOEN|TXONTS1|TXONTS0) #0x98
        self.reg_short_write(TXSTBL, RFSTBL3|RFSTBL0|MSIFS2|MSIFS0) #0x95
        self.reg_long_write(RFCON0, RFOPT0|RFOPT1) #0x03
        self.reg_long_write(RFCON1, VCOOPT0) #0x01
        self.reg_long_write(RFCON2, PLLEN) #0x80
        self.reg_long_write(RFCON6, TXFIL|20MRECVR) #0x90
        self.reg_long_write(RFCON7, SLPCLKSEL1) #0x80
        self.reg_long_write(RFCON8, RFVCO) #0x10
        self.reg_long_write(SLPCON1, CLKOUTEN_N|SLPCLKDIV0) #0x21

        self.reg_short_write(BBREG2,CCAMODE1) #0x80
        self.reg_short_write(CCAEDTH, CCAEDTH6|CCAEDTH5) #0x60
        self.reg_short_write(BBREG6, RSSIMODE0) #0x40

        #enable interrupts
        pyb.enable_irq()

        val = self.reg_short_read(INTCON)
        val &= ~(0x1|0x8) #Clear TXNIE and RXIE. Enable interrupts
        self.reg_short_write(INTCON, val)
        
        # set channel
        self.set_channel(channel)

        # set transmission power
        self.reg_long_write(RFCON3, 0x0) # 0dBm

        self.reset_radio()
        ## done?

    def reg_short_read(self, reg):
        txbuf = bytearray(2)
        rxbuf = bytearray(2)
        txbuf[0] = 0xff & (reg<<1)
        txbuf[1] = 0x0
        print("Short TX read: " + str(txbuf))
        self.cs.low()
        self.spi.send_recv(txbuf, rxbuf)
        self.cs.high()
        print("Short RX read: " + str(rxbuf))
        return rxbuf[1]

    def reg_long_read(self, reg):
        txbuf = bytearray(3)
        rxbuf = bytearray(3)
        txbuf[0] = 0xff & (0x80 | reg>>3)
        txbuf[1] = 0xff & ((reg<<5))
        txbuf[2] = 0x0
        print("Long TX read: " + str(txbuf))
        self.cs.low()
        self.spi.send_recv(txbuf, rxbuf)
        self.cs.high()
        print("Long RX read: " + str(rxbuf))
        return rxbuf[2]

    def reg_short_write(self, reg, buf):
        txbuf = bytearray(2)
        rxbuf = bytearray(2)
        txbuf[0] = 0xff & ((reg<<1) | 0x1)
        txbuf[1] = buf
        print("Short TX write: " + str(txbuf))
        self.cs.low()
        self.spi.send_recv(txbuf, rxbuf)
        self.cs.high()
        print("Short RX write: " + str(rxbuf))
        #return rxbuf[1]

    def reg_long_write(self, reg, buf):
        txbuf = bytearray(3)
        rxbuf = bytearray(3)
        txbuf[0] = 0xff & (0x80 | reg>>3)
        txbuf[1] = 0xff & ((reg<<5) | 0x10)
        txbuf[2] = buf
        print("Long TX write: " + str(txbuf))
        self.cs.low()
        self.spi.send_recv(txbuf, rxbuf)
        self.cs.high()
        print("Long RX write: " + str(rxbuf))
        #return rxbuf[1]

    def reset_pin(self):
        self.resetpin.low()
        pyb.delay(1)
        self.resetpin.high()
        pyb.delay(1)

    def reset_sw(self):
        self.reg_short_write(SOFTRST, RSTPWR | RSTBB | RSTMAC)
        pyb.delay(1)

    def reset_radio(self):
        self.reg_short_write(RFCTL, RFRST)
        pyb.delay(1)
        self.reg_short_write(RFCTL, 0)
        pyb.delay(1)
        
    def set_channel(self, channel):
        assert (channel >= CHANNEL_11)
        assert (channel <= CHANNEL_26)
        #assert ((channel & 0x0f) == 0x03))
        self.reg_long_write(RFCON0, channel)

    def int_tasks(self):
        ret = 0
        stat = self.reg_short_read(INTSTAT)

        if (stat & RXIF):
            ret |= MRF24J40_INT_RX

        if (stat & TXNIF):
            ret |= MRF24J40_INT_TX
        #TODO: security

        return ret
        
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

    def set_pan(self, pan):
        self.reg_short_write(PANIDH, pan >> 8)
        self.reg_short_write(PANIDL, pan & 0xFF)

    def set_short_address(self, addr):
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
