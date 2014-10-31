"""MRF24J40 driver for Micro Python
"""
import mrf24j40
import pyb

def int_handler(line):
    ret = mrf.int_tasks()
    #if ((ret & MRF24J40_INT_RX) != 0):
    #    mrf.recv()
    if ((ret & MRF24J40_INT_TX) != 0):
        print ("TX done")

tim = pyb.Timer(4)

spi = pyb.SPI(1, pyb.SPI.MASTER, baudrate=400000, polarity=0, phase=1, firstbit=pyb.SPI.MSB)
pin_cs    = pyb.Pin(pyb.Pin.board.X5,  pyb.Pin.OUT_PP)
pin_wake  = pyb.Pin(pyb.Pin.board.Y11, pyb.Pin.OUT_PP)
pin_reset = pyb.Pin(pyb.Pin.board.Y12, pyb.Pin.OUT_PP)
mrf = mrf24j40.MRF24J40(spi, pin_cs, pin_wake, pin_reset, interrupt='Y10', ihandler=int_handler)

mrf.set_pan(bytearray([0xca, 0xfe])
mrf.set_short_address(bytearray([0x00, 0x01])

payload = bytearray([0xbb, 0xaa, 0x99])
dest = bytearray([0xff, 0xff])

mrf.send(dest, payload)
# tim.callback(lambda t: mrf.send(dest, payload))
# tim.init(freq=1)

# while True:
#     try:
#         pyb.wfi()
#     except OSError: # VCPInterrupt # Ctrl+C in interpreter mode.
#         break
