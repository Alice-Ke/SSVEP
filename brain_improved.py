import sys; sys.path.append('..') # help python find open_bci_v3.py relative to scripts folder
import open_bci_v3 as bci
import os
import logging
import time
from pygame.locals import *
import numpy
from collections import *
import math
import pandas as pd

port = '/dev/tty.usbserial-DQ0082W2'
baud = 115200
logging.basicConfig(filename="test.log",format='%(asctime)s - %(levelname)s : %(message)s',level=logging.DEBUG)
logging.info('---------LOG START-------------')
board = bci.OpenBCIBoard(port=port, scaled_output=False, log=True)
print("Board Instantiated")
tInput = deque( [ ], maxlen = 250 )
e7_5Output = deque( [ ] )
e12_5Output = deque( [ ] )
e10Output = deque( [ ] )
e5Output = deque( [ ] )

def getsample( sample ):
    global e7_5Output
    global e12_5Output
    global e5Output
    global e10Output
    tInput.append( sample.channel_data[6] )
    frOutput = numpy.fft.fft( tInput )
    aOutput = abs(frOutput)
    pdOutput = pd.Series(aOutput)
    if pdOutput.get(33) != None:
        e7_5Output.append(pdOutput.get(33))
    if pdOutput.get(20) != None:
        e12_5Output.append(pdOutput.get(20))
    # 5hz
    if pdOutput.get(50) != None:
        e5Output.append(pdOutput.get(50))
    # 10hz
    if pdOutput.get(25) != None:
        e10Output.append(pdOutput.get(25))

def headto( ):
    board.start_streaming(getsample, 1.5)
    average7_5 = numpy.mean(e7_5Output)
    average12_5 = numpy.mean(e12_5Output)
    average5 = numpy.mean(e5Output)
    average10 = numpy.mean(e10Output)
    average = (average7_5 + average12_5 + average5 + average10)/4
    if 1000000 < average < 2000000:
        return "right"
    elif 2000000 <= average < 6000000:
        return "left"
    elif 200000 <= average < 300000:
        return "up"
    elif 300000 <= average < 1000000:
        return "down"
    else:
        return "stay"