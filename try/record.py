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
#port = '/dev/tty.OpenBCI-DN0096XA'
baud = 115200
logging.basicConfig(filename="test.log",format='%(asctime)s - %(levelname)s : %(message)s',level=logging.DEBUG)
logging.info('---------LOG START-------------')
board = bci.OpenBCIBoard(port=port, scaled_output=False, log=True)
print("Board Instantiated")
tInput = deque( [ ], maxlen = 250 )
# e5Output = deque( [ ] )
# e7_5Output = deque( [ ] )
# # e5 = 1
# e12_5Output = deque( [ ] )
e7_5 = 1
e12_5 = 1

def getsample( sample ):
    # print list(tInput)
    # while True:
    global e7_5, e12_5

    # global e5
    tInput.append( sample.channel_data[6] )
    # print list(tInput)
    frOutput = numpy.fft.fft( tInput )
    aOutput = abs(frOutput)
    pdOutput = pd.Series(aOutput)
    e12_5 = pdOutput.get(20)
    e7_5 = pdOutput.get(33)
    # if pdOutput.get(50) != None:
    #     e5Output.append(pdOutput.get(50))
    # if pdOutput.get(33) != None:
    #     e7_5Output.append(pdOutput.get(33))
    # if pdOutput.get(20) != None:
    #     e12_5Output.append(pdOutput.get(20))
    # e5 = 10
    # e12_5 = pdOutput.get(20)
    # e5Input.append( e5 )
    # e12_5Input.append( e12_5 )
    # pd5Output = pd.Series(e5Input)
    # pd12_5Output = pd.Series(e12_5Input)
    # average5 = pd.Series.mean(pd5Output)
    # average12_5 = pd.Series.mean(pd12_5Output)

def know( ):
    board.start_streaming(getsample, 1)
    # average5 = numpy.mean(e5Output)
    # # print e5Output
    # average7_5 = numpy.mean(e7_5Output)
    # average12_5 = numpy.mean(e12_5Output)
    # print average5, average7_5, average12_5
    # if average5 > 10000:
    #     return True
    # else:
    #     return False
    # print e5
    print e7_5, e12_5

while True:
    know()
# know()
# # max_time = 3
# start_time = time.time()  # remember when we started
# if (time.time() - start_time) > max_time:
    
# while (time.time() - start_time) < max_time:
#       # board.start_streaming(getsample)
#       print 3





# def getknow():
#     board.start_streaming(getsample)


    

    # print average5, average12_5
    # pdmax = pd.Series.max(pdOutput)

    # pdmaxidx = pd.Index(pdOutput).get_loc(pdmax)
    # print type(aOutput)
    # print fOutput
    # for output in fOutput:
    #     mfOutput.append( absolute( output ) )
   
    #print numpy.where(aOutput==pdmax)
    # average = pd.Series.mean(pdOutput)
    # threshold = average * math.pow( 10.0, (8.0/10.0))
    # if pdmax > threshold:
    #     # return 250 / mfmaxIndex
    #     # print threshold
    #     # print pdmax
    #     # print pdmaxidx
    #     print ("oh")
    # # tInput.clear()
    # else:
    #     print ('hei')  
    #     print aOutput
    # print aOutput


# if __name__ == '__main__':
#     # port = '/dev/tty.usbserial-DQ0082W2'
#     #port = '/dev/tty.OpenBCI-DN0096XA'
#     baud = 115200
#     logging.basicConfig(filename="test.log",format='%(asctime)s - %(levelname)s : %(message)s',level=logging.DEBUG)
#     logging.info('---------LOG START-------------')
#     board = bci.OpenBCIBoard(port=port, scaled_output=False, log=True)
#     print("Board Instantiated")
#     tInput = deque( [ ], maxlen= 250)
#     e5Input = deque( [ ], maxlen = 250)
#     e12_5Input = deque( [ ], maxlen = 250)
#     board.start_streaming(getsample)