# PyTrade Library
import Quandl as Q
import numpy as np
import QuandlAPI as QAPI
#import TestScripts as test


class Stock:
	def __init__(self, name, symbol, n = 90, testclosing = []):
		self.name = name
		self.symbol = symbol
		self.closing = QAPI.getClosing(symbol, n)
		# sanity check
		self.data = Q.get("YAHOO/AAPL", rows=30, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
		self.testclosing = testclosing


	def nDayAverage(self, n, dec=2):
		values = self.closing[:n]
		return (round(np.mean(values),dec))

	""" 
	Parameters:
		n (int) - the number of days considered for each average
		days (int) - the number of days of data available
		dec (int) - optional parameter, specifies the number of decimal places to round to
	
	Description:
		Returns a list of 'n-day averages' for the stock's closing prices. 
		Ordered from most recent (0 index) to oldest.
	"""
	def getMovingAverage(self, n, days, dec=2):
		movingAverages = []
		if(n > days):
			print("n cannot be greater than the number of days")
			return movingAverages
		count = (days - n) + 1
		for i in range(count):
			sample = self.closing[i:i+n]
			#sample = self.testclosing[i:i+n] # test method
			movingAverages.append(float("{0:.2f}".format(np.mean(sample))))
		return movingAverages

	"""
	WIP 
	"""
	def getEMA(self, n, days):
		EMA = []
		closing = self.closing[0:days]
		#closing = self.testclosing[0:days] # test method
		weight = (2/(n + 1)) # also known as the smoothing constant
		# need first moving average to calculate first EMA
		prevEMA = np.mean(closing[-n:])
		EMA.append(float("{0:.2f}".format(float(prevEMA))))
		for i in range((days - n)):
			currEMA = (((closing[-(n + i + 1)] - prevEMA) * weight) + prevEMA)
			EMA.append(float("{0:.2f}".format(float(currEMA))))
			prevEMA = currEMA
		return EMA[::-1] # reverse the list 

""" Test Area - For when I don't want to put crap in the Program """
def main():
	s = Stock('Apple', 'AAPL')
	#print(s.data)
	print(s.getMovingAverage(10,30))
	print(s.getEMA(10,30))

if __name__ == "__main__":
    main()

