"""
Broadcast using the MRF24J40 driver.

Usage:
import broadcast
"""

import mrf24j40
import pyb
import micropython
from usched import Sched, Pinblock, Timeout
micropython.alloc_emergency_exception_buf(200)

class irq_handler(object):
    def __init__(self, mrf, pin):
        self.mrf = mrf
        self.pin = pin

    def callback(self, line):
        # don't do much in interrupt context
        # (especially do not try to allocate memory)
        # the true functionality is in irq_thread()
        #print("callback")
        pass

def tx_done_cb():
    print("TX done")

def rx_cb(buf, rssi, lqi):
    print("RX")

def irq_thread(mrf, interrupt='Y10'):
    intpin = pyb.Pin(interrupt, pyb.Pin.OUT_PP)
    handler = irq_handler(mrf, intpin)
    wf = Pinblock(interrupt, pyb.ExtInt.IRQ_FALLING,
                  pyb.Pin.PULL_DOWN, handler.callback)
    while True:
        result = (yield wf()) # Wait for the interrupt
        intr = mrf.int_tasks()
        # call rx / tx callbacks
        if ((intr & mrf24j40.MRF24J40_INT_RX) != 0):
            rx_cb(mrf.recv())
        if ((intr & mrf24j40.MRF24J40_INT_TX) != 0):
            tx_done_cb()

def tx_thread(mrf):
    payload = bytearray([0xbb, 0xaa, 0x99])
    dest = bytearray([0xff, 0xff])

    wf = Timeout(1)

    while True:
        result = (yield wf()) # Wait for the interrupt
        print("TX")
        mrf.send_dp(dest, payload)
        
def run():
    objSched = Sched()

    spi       = pyb.SPI(1, pyb.SPI.MASTER, baudrate=400000,
                        polarity=0, phase=1, firstbit=pyb.SPI.MSB)
    pin_cs    = pyb.Pin(pyb.Pin.board.X5,  pyb.Pin.OUT_PP)
    pin_wake  = pyb.Pin(pyb.Pin.board.Y11, pyb.Pin.OUT_PP)
    pin_reset = pyb.Pin(pyb.Pin.board.Y12, pyb.Pin.OUT_PP)
    mrf = mrf24j40.MRF24J40(spi, pin_cs, pin_wake, pin_reset)
    mrf.set_pan(bytearray([0xca, 0xfe]))
    mrf.set_short_address(bytearray([0x00, 0x01]))

    objSched.add_thread(irq_thread(mrf))
    mrf.enable_interrupts()

    objSched.add_thread(tx_thread(mrf))
        
    objSched.run()

run()


