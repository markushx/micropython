"""
Test for mrf24j40 module.

Usage:
import mrf24j40test
"""

import pyb
from pyb import Pin, SPI

def reg_short_read(spi, cs, reg):
    txbuf = bytearray(2)
    rxbuf = bytearray(2)
    txbuf[0] = 0xff & (reg<<1)
    txbuf[1] = 0x0
    print("Short TX read: " + str(txbuf))
    cs.low()
    spi.send_recv(txbuf, rxbuf)
    cs.high()
    print("Short RX read: " + str(rxbuf))
    return rxbuf[1]

def reg_long_read(spi, cs, reg):
    txbuf = bytearray(3)
    rxbuf = bytearray(3)
    txbuf[0] = 0xff & (0x80 | reg>>3)
    txbuf[1] = 0xff & ((reg<<5))
    txbuf[2] = 0x0
    print("Long TX read: " + str(txbuf))
    cs.low()
    spi.send_recv(txbuf, rxbuf)
    cs.high()
    print("Long RX read: " + str(rxbuf))
    return rxbuf[2]

def reg_short_write(spi, cs, reg, buf):
    txbuf = bytearray(2)
    rxbuf = bytearray(2)
    txbuf[0] = 0xff & ((reg<<1) | 0x1)
    txbuf[1] = buf
    print("Short TX write: " + str(txbuf))
    cs.low()
    spi.send_recv(txbuf, rxbuf)
    cs.high()
    print("Short RX write: " + str(rxbuf))
    #return rxbuf[1]

def reg_long_write(spi, cs, reg, buf):
    txbuf = bytearray(3)
    rxbuf = bytearray(3)
    txbuf[0] = 0xff & (0x80 | reg>>3)
    txbuf[1] = 0xff & ((reg<<5) | 0x10)
    txbuf[2] = buf
    print("Long TX write: " + str(txbuf))
    cs.low()
    spi.send_recv(txbuf, rxbuf)
    cs.high()
    print("Long RX write: " + str(rxbuf))
    #return rxbuf[1]

def test():
    spi = SPI(1, SPI.MASTER, baudrate=400000, polarity=0, phase=1, firstbit=SPI.MSB)
    pin_cs    = Pin(Pin.board.X5,  Pin.OUT_PP)
    pin_wake  = Pin(Pin.board.Y11, Pin.OUT_PP)
    pin_reset = Pin(Pin.board.Y12, Pin.OUT_PP)

    print("resetting")
    pin_reset.low()
    pyb.delay(1)
    pin_reset.high()
    pyb.delay(1)
    print("resetting done")

    #soft reset
    print("soft reset")
    reg_short_write(spi, pin_cs, 0x2a, 0x07)
    pyb.delay(1)
    print("Result: " + str(reg_short_read (spi, pin_cs, 0x2a)))

    #test short: PANIDL
    print("PANIDL")
    reg_short_write(spi, pin_cs, 0x01, 0xca)
    pyb.delay(1)
    print("Result: " + str(reg_short_read (spi, pin_cs, 0x01)))
    
    #test long: RFCON0
    print("RFCON0")
    reg_long_write(spi, pin_cs, 0x200, 0xf3)
    pyb.delay(1)
    print("Result: " + str(reg_long_read (spi, pin_cs, 0x200)))

test()
