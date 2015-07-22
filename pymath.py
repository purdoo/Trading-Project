## Methods to be imported by main program
import numpy as np

def getSMA(closing, n, period):
	movingAverages = []
	if(n > period):
		print("n cannot be greater than the number of days")
		return movingAverages
	count = (period - n) + 1
	for i in range(count):
		sample = closing[i:(i+n)]
		#sample = self.testclosing[i:i+n] # test method
		movingAverages.append(float("{0:.2f}".format(np.mean(sample))))
	return movingAverages[::-1] # reverse the list 

def getEMA(closing, n, period):
	EMA = []
	closing = closing[0:period]

	weight = (2/(n + 1)) # also known as the smoothing constant
	# need first moving average to calculate first EMA
	prevEMA = np.mean(closing[-n:])
	EMA.append(float("{0:.2f}".format(float(prevEMA))))
	for i in range((period - n)):
		currEMA = (((closing[-(n + i + 1)] - prevEMA) * weight) + prevEMA)
		EMA.append(float("{0:.2f}".format(float(currEMA))))
		prevEMA = currEMA
	return EMA