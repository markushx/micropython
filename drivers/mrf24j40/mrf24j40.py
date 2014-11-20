"""
MRF24J40 driver for Micro Python

An example for the usage of the driver is in examples/802154/broadcast.py
"""

import pyb

MRF24J40_INT_RX = const(0x1)
MRF24J40_INT_TX = const(0x2)

"""Constants for the MRF24J40 driver for Micro Python"""

# REGISTERS
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
SLPACK_R    = const(0x35)
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

# MRF24J40 long registers
RFCON0    = const(0x200)
RFCON1    = const(0x201)
RFCON2    = const(0x202)
RFCON3    = const(0x203)
#RESERVED = const(0x204)
RFCON5    = const(0x205)
RFCON6    = const(0x206)
RFCON7    = const(0x207)
RFCON8    = const(0x208)
SLPCAL0_R   = const(0x209)
SLPCAL1_R   = const(0x20A)
SLPCAL2_R   = const(0x20B)
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
MAINCNT0_R  = const(0x226)
MAINCNT1_R  = const(0x227)
MAINCNT2_R  = const(0x228)
MAINCNT3_R  = const(0x229)
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

# ~REGISTERS

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

# REGISTER CONTENTS
#RXMCR register 0x00
NOACKRSP  = const(0x20)
PANCOORD  = const(0x08)
COORD     = const(0x04)
ERRPKT    = const(0x02)
PROMI     = const(0x01)

#RXFLUSH register 0x0D
WAKEPOL   = const(0x40)
WAKEPAD   = const(0x20)
CMDONLY   = const(0x08)
DATAONLY  = const(0x04)
BCNONLY   = const(0x02)
RXFLUSH_BIT = const(0x01)

#ORDER register 0x10
BO3       = const(0x80)
BO2       = const(0x40)
BO1       = const(0x20)
BO0       = const(0x10)
SO3       = const(0x08)
SO2       = const(0x04)
SO1       = const(0x02)
SO0       = const(0x01)

#TXMCR register 0x11
NOCSMA    = const(0x80)
BATLIFEXT = const(0x40)
SLOTTED   = const(0x20)
MACMINBE1 = const(0x10)
MACMINBE0 = const(0x08)
CSMABF2   = const(0x04)
CSMABF1   = const(0x02)
CSMABF0   = const(0x01)

#ACKTIMOUT register 0x12
DRPACK    = const(0x80)
MAWD6     = const(0x40)
MAWD5     = const(0x20)
MAWD4     = const(0x10)
MAWD3     = const(0x08)
MAWD2     = const(0x04)
MAWD1     = const(0x02)
MAWD0     = const(0x01)

#ESLOTG1 register 0x13
GTS1_3    = const(0x80)
GTS1_2    = const(0x40)
GTS1_1    = const(0x20)
GTS1_0    = const(0x10)
CAP3      = const(0x08)
CAP2      = const(0x04)
CAP1      = const(0x02)
CAP0      = const(0x01)

#SYMTICKL register 0x14
TICKP7    = const(0x80)
TICKP6    = const(0x40)
TICKP5    = const(0x20)
TICKP4    = const(0x10)
TICKP3    = const(0x08)
TICKP2    = const(0x04)
TICKP1    = const(0x02)
TICKP0    = const(0x01)

#SYMTICKH register 0x15
TXONT6    = const(0x80)
TXONT5    = const(0x40)
TXONT4    = const(0x20)
TXONT3    = const(0x10)
TXONT2    = const(0x08)
TXONT1    = const(0x04)
TXONT0    = const(0x02)
TICKP8    = const(0x01)

#PACON0 register 0x16
PAONT7    = const(0x80)
PAONT6    = const(0x40)
PAONT5    = const(0x20)
PAONT4    = const(0x10)
PAONT3    = const(0x08)
PAONT2    = const(0x04)
PAONT1    = const(0x02)
PAONT0    = const(0x01)

#PACON1 register 0x17
PAONTS3   = const(0x10)
PAONTS2   = const(0x08)
PAONTS1   = const(0x04)
PAONTS0   = const(0x02)
PAONT8    = const(0x01)

#PACON2 register 0x18
FIFOEN    = const(0x80)
TXONTS3   = const(0x20)
TXONTS2   = const(0x10)
TXONTS1   = const(0x08)
TXONTS0   = const(0x04)
TXONT8    = const(0x02)
TXONT7    = const(0x01)

#TXBCON0 register 0x1A
TXBSECEN  = const(0x02)
TXBTRIG   = const(0x01)

#TXNCON register 0x1B
FPSTAT    = const(0x10)
INDIRECT  = const(0x08)
TXNACKREQ = const(0x04)
TXNSECEN  = const(0x02)
TXNTRIG   = const(0x01)

#TXG1CON register 0x1C
TXG1RETRY1 = const(0x80)
TXG1RETRY0 = const(0x40)
TXG1SLOT2  = const(0x20)
TXG1SLOT1  = const(0x10)
TXG1SLOT0  = const(0x08)
TXG1ACKREQ = const(0x04)
TXG1SECEN  = const(0x02)
TXG1TRIG   = const(0x01)

#TXG2CON register 0x1D
TXG2RETRY1 = const(0x80)
TXG2RETRY0 = const(0x40)
TXG2SLOT2  = const(0x20)
TXG2SLOT1  = const(0x10)
TXG2SLOT0  = const(0x08)
TXG2ACKREQ = const(0x04)
TXG2SECEN  = const(0x02)
TXG2TRIG   = const(0x01)

#ESLOTG23 register 0x1E
GTS3_3     = const(0x80)
GTS3_2     = const(0x40)
GTS3_1     = const(0x20)
GTS3_0     = const(0x10)
GTS2_3     = const(0x08)
GTS2_2     = const(0x04)
GTS2_1     = const(0x02)
GTS2_0     = const(0x01)

#ESLOTG45 register 0x1F
GTS5_3     = const(0x80)
GTS5_2     = const(0x40)
GTS5_1     = const(0x20)
GTS5_0     = const(0x10)
GTS4_3     = const(0x08)
GTS4_2     = const(0x04)
GTS4_1     = const(0x02)
GTS4_0     = const(0x01)

#ESLOTG67 register 0x20
GTS6_3     = const(0x08)
GTS6_2     = const(0x04)
GTS6_1     = const(0x02)
GTS6_0     = const(0x01)

#TXPEND register 0x21
MLIFS5     = const(0x80)
MLIFS4     = const(0x40)
MLIFS3     = const(0x20)
MLIFS2     = const(0x10)
MLIFS1     = const(0x08)
MLIFS0     = const(0x04)
GTSSWITCH  = const(0x02)
FPACK      = const(0x01)

#WAKECON register 0x22
IMMWAKE    = const(0x80)
REGWAKE    = const(0x40)

#FRMOFFSET register 0x23
OFFSET7    = const(0x80)
OFFSE6T    = const(0x40)
OFFSET5    = const(0x20)
OFFSET4    = const(0x10)
OFFSET3    = const(0x08)
OFFSET2    = const(0x04)
OFFSET1    = const(0x02)
OFFSET0    = const(0x01)

#TXSTAT register 0x24
TXNRETRY1  = const(0x80)
TXNRETRY0  = const(0x40)
CCAFAIL    = const(0x20)
TXG2FNT    = const(0x10)
TXG1FNT    = const(0x08)
TXG2STAT   = const(0x04)
TXG1STAT   = const(0x02)
TXNSTAT    = const(0x01)

#TXBCON1 register 0x25
TXBMSK     = const(0x80)
N_WU_BCN   = const(0x40)
RSSINUM1   = const(0x20)
RSSINUM0   = const(0x10)

#TXBCON1 register 0x26
GTSON      = const(0x08)

#TXTIME register 0x27
TURNTIME3  = const(0x80)
TURNTIME2  = const(0x40)
TURNTIME1  = const(0x20)
TURNTIME0  = const(0x10)

#HSYMTMRL register 0x28
HSYMTMR7  = const(0x80)
HSYMTMR6  = const(0x40)
HSYMTMR5  = const(0x20)
HSYMTMR4  = const(0x10)
HSYMTMR3  = const(0x08)
HSYMTMR2  = const(0x04)
HSYMTMR1  = const(0x02)
HSYMTMR0  = const(0x01)

#HSYMTMRH register 0x29
HSYMTMR15 = const(0x80)
HSYMTMR14 = const(0x40)
HSYMTMR13 = const(0x20)
HSYMTMR12 = const(0x10)
HSYMTMR11 = const(0x08)
HSYMTMR10 = const(0x04)
HSYMTMR09 = const(0x02)
HSYMTMR08 = const(0x01)

# SOFTRST register 0x2A
RSTPWR    = const(0x04)
RSTBB     = const(0x02)
RSTMAC    = const(0x01)

# Reserved register 0x2B

#SECCON0 register 0x2C
SECIGNORE  = const(0x80)
SECSTART   = const(0x40)
RXCIPHER2  = const(0x20)
RXCIPHER1  = const(0x10)
RXCIPHER0  = const(0x08)
TXNCIPHER2 = const(0x04)
TXNCIPHER1 = const(0x02)
TXNCIPHER0 = const(0x01)

#SECCON1 register 0x2D
TXBCIPHER2 = const(0x40)
TXBCIPHER1 = const(0x20)
TXBCIPHER0 = const(0x10)
DISDEC     = const(0x02)
DISENC     = const(0x01)

#TXSTBL register 0x2E
RFSTBL3  = const(0x80)
RFSTBL2  = const(0x40)
RFSTBL1  = const(0x20)
RFSTBL0  = const(0x10)
MSIFS3   = const(0x08)
MSIFS2   = const(0x04)
MSIFS1   = const(0x02)
MSIFS0   = const(0x01)

# Reserved register 0x2F

#RXSR register 0x30
UPSECERR  = const(0x40)
BATIND    = const(0x20)
SECDECERR = const(0x04)

#INTSTAT register 0x31
SLPIF     = const(0x80)
WAKEIF    = const(0x40)
HSYMTMRIF = const(0x20)
SECIF     = const(0x10)
RXIF      = const(0x08)
TXG2IF    = const(0x04)
TXG1IF    = const(0x02)
TXNIF     = const(0x01)

#INTCON register 0x32
SLPIE     = const(0x80)
WAKEIE    = const(0x40)
HSYMTMRIE = const(0x20)
SECIE     = const(0x10)
RXIE      = const(0x08)
TXG2IE    = const(0x04)
TXG1IE    = const(0x02)
TXNIE     = const(0x01)

#GPIO register 0x33
GPIO5     = const(0x20)
GPIO4     = const(0x10)
GPIO3     = const(0x08)
GPIO2     = const(0x04)
GPIO1     = const(0x02)
GPIO0     = const(0x01)

#TRISGPIO register 0x34
TRISGP5   = const(0x20)
TRISGP4   = const(0x10)
TRISGP3   = const(0x08)
TRISGP2   = const(0x04)
TRISGP1   = const(0x02)
TRISGP0   = const(0x01)

#SLPACK register 0x35
SLPACK    = const(0x80)
WAKECNT6  = const(0x40)
WAKECNT5  = const(0x20)
WAKECNT4  = const(0x10)
WAKECNT3  = const(0x08)
WAKECNT2  = const(0x04)
WAKECNT1  = const(0x02)
WAKECNT0  = const(0x01)

# RFCTL register 0x36
WAKECNT8  = const(0x10)
WAKECNT7  = const(0x08)
RFRST     = const(0x04)
RFTXMODE  = const(0x02)
RFRXMODE  = const(0x01)

#SECCR2 register 0x37
UPDEC       = const(0x80)
UPENC       = const(0x40)
TXG2CIPHER2 = const(0x20)
TXG2CIPHER1 = const(0x10)
TXG2CIPHER0 = const(0x08)
TXG1CIPHER2 = const(0x04)
TXG1CIPHER1 = const(0x02)
TXG1CIPHER0 = const(0x01)

# BBREG0 register 0x38
TURBO      = const(0x04)

# BBREG1 register 0x39
RXDECINV  = const(0x04)

# BBREG2 register 0x3A
CCAMODE1  = const(0x80)
CCAMODE0  = const(0x40)
CCACSTH3  = const(0x20)
CCACSTH2  = const(0x10)
CCACSTH1  = const(0x08)
CCACSTH0  = const(0x04)

# BBREG3 register 0x3B
PREVALIDTH3 = const(0x80)
PREVALIDTH2 = const(0x40)
PREVALIDTH1 = const(0x20)
PREVALIDTH0 = const(0x10)
PREDETTH2   = const(0x08)
PREDETTH1   = const(0x04)
PREDETTH0   = const(0x02)

# BBREG4 register 0x3C
CSTH2     = const(0x80)
CSTH1     = const(0x40)
CSTH0     = const(0x20)
PRECNT2   = const(0x10)
PRECNT1   = const(0x08)
PRECNT0   = const(0x04)

# Reserved register 0x3D

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

#RFCON3 register 0x203
TXPWRL1   = const(0x80)
TXPWRL0   = const(0x40)
TXPWRS2   = const(0x20)
TXPWRS1   = const(0x10)
TXPWRS0   = const(0x08)

# Reserved register 0x204

#RFCON5 register 0x205
BATTH3    = const(0x80)
BATTH2    = const(0x40)
BATTH1    = const(0x20)
BATTH0    = const(0x10)

#RFCON6 register 0x206
TXFIL     = const(0x80)
_20MRECVR = const(0x10)
BATEN     = const(0x08)

#RFCON7 register 0x207
SLPCLKSEL1  = const(0x80)
SLPCLKSEL2  = const(0x40)
CLKOUTMODE1 = const(0x02)
CLKOUTMODE0 = const(0x01)

#RFCON8 register 0x208
RFVCO     = const(0x10)

#SLPCAL0 register 0x209
SLPCAL7   = const(0x80)
SLPCAL6   = const(0x40)
SLPCAL5   = const(0x20)
SLPCAL4   = const(0x10)
SLPCAL3   = const(0x08)
SLPCAL2   = const(0x04)
SLPCAL1   = const(0x02)
SLPCAL0   = const(0x01)

#SLPCAL1 register 0x20A
SLPCAL15  = const(0x80)
SLPCAL14  = const(0x40)
SLPCAL13  = const(0x20)
SLPCAL12  = const(0x10)
SLPCAL11  = const(0x08)
SLPCAL10  = const(0x04)
SLPCAL9   = const(0x02)
SLPCAL8   = const(0x01)

#SLPCAL2 register 0x20B
SLPCALRDY = const(0x80)
SLPCALEN  = const(0x10)
SLPCAL19  = const(0x08)
SLPCAL18  = const(0x04)
SLPCAL17  = const(0x02)
SLPCAL16  = const(0x01)

# Reserved register 0x20C
# Reserved register 0x20D
# Reserved register 0x20E

#RFSTATE register 0x20F
RFSTATE2  = const(0x80)
RFSTATE1  = const(0x40)
RFSTATE0  = const(0x20)

#RSSI register 0x210
RSSI7     = const(0x80)
RSSI6     = const(0x40)
RSSI5     = const(0x20)
RSSI4     = const(0x10)
RSSI3     = const(0x08)
RSSI2     = const(0x04)
RSSI1     = const(0x02)
RSSI0     = const(0x01)

#SLPCON0 register 0x211
INTEDG     = const(0x02)
N_SLPCLKEN = const(0x01)

# Reserved register 0x212
# Reserved register 0x213
# Reserved register 0x214
# Reserved register 0x215
# Reserved register 0x216
# Reserved register 0x217
# Reserved register 0x218
# Reserved register 0x219
# Reserved register 0x21A
# Reserved register 0x21B
# Reserved register 0x21C
# Reserved register 0x21D
# Reserved register 0x21E
# Reserved register 0x21F

#RFCON1 register 0x220
CLKOUTEN_N = const(0x20)
SLPCLKDIV4 = const(0x10)
SLPCLKDIV3 = const(0x08)
SLPCLKDIV2 = const(0x04)
SLPCLKDIV1 = const(0x02)
SLPCLKDIV0 = const(0x01)

# Reserved register 0x221

#WAKETIMEL register 0x222
WAKETIME7     = const(0x80)
WAKETIME6     = const(0x40)
WAKETIME5     = const(0x20)
WAKETIME4     = const(0x10)
WAKETIME3     = const(0x08)
WAKETIME2     = const(0x04)
WAKETIME1     = const(0x02)
WAKETIME0     = const(0x01)

#WAKETIMEH register 0x223
WAKETIME10    = const(0x04)
WAKETIME9     = const(0x02)
WAKETIME8     = const(0x01)

#REMCNTL register 0x224
REMCNT7     = const(0x80)
REMCNT6     = const(0x40)
REMCNT5     = const(0x20)
REMCNT4     = const(0x10)
REMCNT3     = const(0x08)
REMCNT2     = const(0x04)
REMCNT1     = const(0x02)
REMCNT0     = const(0x01)

#REMCNTH register 0x225
REMCNT15    = const(0x80)
REMCNT14    = const(0x40)
REMCNT13    = const(0x20)
REMCNT12    = const(0x10)
REMCNT11    = const(0x08)
REMCNT10    = const(0x04)
REMCNT9     = const(0x02)
REMCNT8     = const(0x01)

#MAINCNT0 register 0x226
MAINCNT7     = const(0x80)
MAINCNT6     = const(0x40)
MAINCNT5     = const(0x20)
MAINCNT4     = const(0x10)
MAINCNT3     = const(0x08)
MAINCNT2     = const(0x04)
MAINCNT1     = const(0x02)
MAINCNT0     = const(0x01)

#MAINCNT1 register 0x227
MAINCNT15    = const(0x80)
MAINCNT14    = const(0x40)
MAINCNT13    = const(0x20)
MAINCNT12    = const(0x10)
MAINCNT11    = const(0x08)
MAINCNT10    = const(0x04)
MAINCNT9     = const(0x02)
MAINCNT8     = const(0x01)

#MAINCNT2 register 0x228
MAINCNT23    = const(0x80)
MAINCNT22    = const(0x40)
MAINCNT21    = const(0x20)
MAINCNT20    = const(0x10)
MAINCNT19    = const(0x08)
MAINCNT18    = const(0x04)
MAINCNT17    = const(0x02)
MAINCNT16    = const(0x01)

#MAINCNT3 register 0x229
STARTCNT    = const(0x80)
MAINCNT25    = const(0x02)
MAINCNT24    = const(0x01)

# Reserved register 0x22A
# Reserved register 0x22B
# Reserved register 0x22C
# Reserved register 0x22D
# Reserved register 0x22E

#TESTMODE register 0x22F
RSSIWAIT1    = const(0x10)
RSSIWAIT0    = const(0x08)
TESTMDOE2    = const(0x04)
TESTMDOE1    = const(0x02)
TESTMDOE0    = const(0x01)

# ASSOEADR0-7 0x230-0x237
# ASSOSADR0-1 0x238-0x239
# Reserved register 0x23A
# Reserved register 0x23B
# Unimplemented register 0x23C
# Unimplemented register 0x23D
# Unimplemented register 0x23E
# Unimplemented register 0x23F
# UPNONCE0-12 0x240-0x24C

# ~REGISTER CONTENTS

#IEEE 802.15.4
FRAME_TYPE_BEACON  = const(0b000)
FRAME_TYPE_DATA    = const(0b001)
FRAME_TYPE_ACK     = const(0b010)
FRAME_TYPE_COMMAND = const(0b011)
OFFSET_FRAME_TYPE        = const(0)
OFFSET_SECURITY_ENABLED  = const(3)
OFFSET_FRAME_PENDING     = const(4)
OFFSET_AR                = const(5)
OFFSET_PANID_COMPRESSION = const(6)

ADDR_MODE_NOT_PRESENT =  const(0b00)
ADDR_MODE_SHORT_16    =  const(0b10)
ADDR_MODE_EXT_64      =  const(0b11)
OFFSET_DEST_ADDR_MDOE = const(6)
OFFSET_SRC_ADDR_MDOE  = const(2)

FRAME_VERSION_2003    = const(0x00)
FRAME_VERSION_2006    = const(0x01)
OFFSET_FRAME_VERSION  = const(4)

class MRF24J40:
    seq_number = 0x0
    pan        = 0x0
    src        = 0x0

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

        # self.cs.high()
        # pyb.delay(1)
        # self.cs.low()
        # pyb.delay(1)

        # initialize the MRF24J40 according to Example 3-1 of the datasheet
        self.reset_sw()
        self.reg_short_write(PACON2, FIFOEN|TXONTS1|TXONTS0) #0x98
        self.reg_short_write(TXSTBL, RFSTBL3|RFSTBL0|MSIFS2|MSIFS0) #0x95
        self.reg_long_write(RFCON0, RFOPT0|RFOPT1) #0x03
        self.reg_long_write(RFCON1, VCOOPT0) #0x01
        self.reg_long_write(RFCON2, PLLEN) #0x80
        self.reg_long_write(RFCON6, TXFIL|_20MRECVR) #0x90
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
        #print("SET Channel " + str(channel))
        self.set_channel(channel)
        #print("GET Channel " + str(self.get_channel()))

        # set transmission power
        self.reg_long_write(RFCON3, 0x0) # 0dBm

        self.reset_radio()

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
        assert (((channel & 0x0f) == 0x03))
        self.reg_long_write(RFCON0, channel)

    def get_channel(self):
        return self.reg_long_read(RFCON0)

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

        # Read RXFIFO addresses, 0x301 through (0x300 + Frame Length + 2);
        # read packet data plus LQI and RSSI.
        buf = []
        for i in range(len):
            buf[i] = self.reg_short_read(RX+1+i)

        lqi = self.reg_short_read(RX_FIFO+len+1)
        rssi = self.reg_short_read(RX_FIFO+len+2)
        
        # Clear RXDECINV = 0; enable receiving packets.
        self.reg_short_write(BBREG1, 0)

        pyb.enable_irq(irqstate)

        return (buf, rssi, lqi)

    def set_pan(self, pan):
        assert len(pan) == 2
        self.reg_short_write(PANIDH, pan[0])
        self.reg_short_write(PANIDL, pan[1])

    def set_short_address(self, addr):
        assert len(addr) == 2
        self.reg_short_write(SADRH, addr[0])
        self.reg_short_write(SADRL, addr[1])

    def send_basic(self, buf, hdr_len, frame_len):
        assert hdr_len < frame_len
        assert len(buf) == frame_len

        # Request ACK
        txn = self.reg_short_read(TXNCON)
        self.reg_short_write(TXNCON, txn | TXNACKREQ)
        
        self.reg_long_write(TX_FIFO, hdr_len)
        self.reg_long_write(TX_FIFO+1, frame_len)

        for i in range(frame_len):
            self.reg_long_write(TX_FIFO+2+i, buf[i])

        #TODO: encryption, etc
        self.reg_short_write(TXNCON, txn | TXNTRIG)

    def send(self, dest, payload):
        assert len(dest) == 2 or len(dest) == 8
        assert len(payload) <= 11

        frame_control = bytearray([
            #first byte
            FRAME_TYPE_DATA << OFFSET_FRAME_TYPE |
            0 << OFFSET_SECURITY_ENABLED |
            0 << OFFSET_FRAME_PENDING |
            1 << OFFSET_AR |
            1 << OFFSET_PANID_COMPRESSION |
            0 << 0,
            #second byte
            ADDR_MODE_SHORT_16 << OFFSET_DEST_ADDR_MDOE |
            FRAME_VERSION_2003 << OFFSET_FRAME_VERSION |
            ADDR_MODE_SHORT_16 << OFFSET_SRC_ADDR_MDOE
            ])

        addressing = bytearray([
            self.pan[0],
            self.pan[1],
            dest[0],
            dest[1],
            self.src[0],
            self.src[1]
            ])
        #TODO: security
        hdr = bytearray([i for subl in [frame_control, [self.seq_number], addressing] for i in subl])
        hdr_len = len(hdr)
        frame_len = hdr_len + len(payload)
        buf = bytearray([i for subl in [hdr, payload] for i in subl])

        print("TX: HDR: " + str(hdr))
        print("TX: BUF: " + str(buf))
        self.send_basic(buf, hdr_len, frame_len)
        self.seq_number = (self.seq_number + 1) % 0xff

    def send(self, src, srcpan, dest, destpan, payload):
        assert len(src) == 2 or len(src) == 8
        assert len(dest) == 2 or len(dest) == 8
        assert len(srcpan) == 2
        assert len(destpan) == 2 
        assert len(payload) <= 11

        if (srcpan == destpan):
            compression = (1 << OFFSET_PANID_COMPRESSION)
        else:
            compression = (0 << OFFSET_PANID_COMPRESSION)

        if (len(dest) == 2):
            dest_mode = (ADDR_MODE_SHORT_16 << OFFSET_DEST_ADDR_MODE)
        else:
            dest_mode = (ADDR_MODE_LONG_64 << OFFSET_DEST_ADDR_MODE)

        if (len(src) == 2):
            src_mode = (ADDR_MODE_SHORT_16 << OFFSET_SRC_ADDR_MODE)
        else:
            src_mode = (ADDR_MODE_LONG_64 << OFFSET_SRC_ADDR_MODE)
        
        frame_control = bytearray([
            #first byte
            FRAME_TYPE_DATA << OFFSET_FRAME_TYPE |
            0 << OFFSET_SECURITY_ENABLED |
            0 << OFFSET_FRAME_PENDING |
            1 << OFFSET_AR |
            compression |
            0 << 0,
            #second byte
            dest_mode |
            FRAME_VERSION_2003 << OFFSET_FRAME_VERSION |
            src_mode
            ])

        addressing_length = 0
        if (srcpan == destpan):
            addressing_length += 2
        else:
            addressing_length += 4
        addressing_length += len(src)
        addressing_length += len(dest)
        
        addressing = bytearray(addressing_length)
        addressing_index = 0
        addressing[addressing_index] = destpan[0]
        addressing_index += 1
        addressing[addressing_index] = destpan[1]
        addressing_index += 1
        for i in range(0, len(dest)):
            addressing[addressing_index] = dest[i]
            addressing_index += 1

        if (srcpan != destpan):
            addressing[addressing_index] = srcpan[0]
            addressing_index += 1
            addressing[addressing_index] = srcpan[1]
            addressing_index += 1

        for i in range(0, len(src)):
            addressing[addressing_index] = src[i]
            addressing_index += 1
                        
        #TODO: security
        hdr = bytearray([i for subl in [frame_control, [self.seq_number], addressing] for i in subl])
        hdr_len = len(hdr)
        frame_len = hdr_len + len(payload)
        buf = bytearray([i for subl in [hdr, payload] for i in subl])

        print("TX: HDR: " + str(hdr))
        print("TX: BUF: " + str(buf))
        self.send_basic(buf, hdr_len, frame_len)
        self.seq_number = (self.seq_number + 1) % 0xff

