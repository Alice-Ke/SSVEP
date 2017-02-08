from numpy import *
import math
from collections import *

array = [1, 2, 3, 4]
maxe = max( array )
print maxe 

        # print len( tInput )

# a = linspace(0, 2*pi, 8)
# i = 0
# while True:
#     if len( tInput ) < 8:
#         tInput.append( a[i] )
#         i = i+1
#     else:
#         frOutput = fft.fft( tInput )
#         fOutput = frOutput[ 0: 4 ]
#         mfOutput = []
#         for output in fOutput:
#             mfOutput.append( absolute( output ) )
#             print output
#         mfmax = max( mfOutput )
#         print mfmax
#         mfmaxIndex = mfOutput.index( mfmax )
#         average = sum( list( mfOutput ) ) / len( mfOutput )
#         print average
#         threshold = average * math.pow( 10.0, (6.0/10.0))
#         print threshold
#         if mfmax > threshold:
#             # return 250 / mfmaxIndex
#             print ("oh")
#         tInput.clear()
#         print len(tInput)
#         i = 0	