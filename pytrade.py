# PyTrade Library
import Quandl as Q
import numpy as np
import QuandlAPI as QAPI
#import TestScripts as test
import matplotlib.pyplot as plt

class Stock:
	def __init__(self, name, symbol, n = 10, period = 30, testclosing = []):
		self.name = name
		self.symbol = symbol
		self.n = n
		self.period = period
		self.closing = QAPI.getClosing(symbol, period)
		self.SMA = self.getSMA()
		self.EMA = self.getEMA()
		self.Bollinger = self.getBollingerBands()

		# sanity check
		self.data = Q.get("YAHOO/AAPL", rows=30, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
		self.Dates = self.data.index.tolist()
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
		Ordered from oldest to newest (left to right)
	"""
	def getSMA(self, dec=2):
		movingAverages = []
		if(self.n > self.period):
			print("n cannot be greater than the number of days")
			return movingAverages
		count = (self.period - self.n) + 1
		for i in range(count):
			sample = self.closing[i:(i+self.n)]
			#sample = self.testclosing[i:i+n] # test method
			movingAverages.append(float("{0:.2f}".format(np.mean(sample))))
		return movingAverages[::-1] # reverse the list 

	"""
	WIP 
	"""
	def getEMA(self):
		EMA = []
		closing = self.closing[0:self.period]
		#closing = self.testclosing[0:days] # test method
		weight = (2/(self.n + 1)) # also known as the smoothing constant
		# need first moving average to calculate first EMA
		prevEMA = np.mean(closing[-self.n:])
		EMA.append(float("{0:.2f}".format(float(prevEMA))))
		for i in range((self.period - self.n)):
			currEMA = (((closing[-(self.n + i + 1)] - prevEMA) * weight) + prevEMA)
			EMA.append(float("{0:.2f}".format(float(currEMA))))
			prevEMA = currEMA
		return EMA

	def getBollingerBands(self):
		#print(np.std(self.getSMA(10,30)))
		stdev, upperBand, lowerBand = [], [], []
		closing = self.closing[0:self.period]
		count = (self.period - self.n) + 1
		for i in range(count):
			sample = self.closing[i:(i+self.n)]
			stdev.append(np.std(sample))
			upperBand.append(self.SMA[i] + (1*np.std(sample)))
			lowerBand.append(self.SMA[i] - (1*np.std(sample)))
		#return stdev[::-1]
		return (upperBand, lowerBand)

def bollinger(symbol, n = 10, period = 30):
	s = Stock('Name', symbol, n, period)
	return 0

""" Test Area - For when I don't want to put crap in the Program """
def main():
	s = Stock('Apple', 'AAPL', 10, 100)
	#s = Stock('Google', 'GOOG', 10)
	#s = Stock('Test', 'CWEI', 10)
	
	#print(s.data)
	#print(s.getSMA(30))
	#print(s.getEMA(30))
	#print(s.getBollingerBands(30))
	#print(s.Dates)
	#bollingerBands = s.getBollingerBands(30)
	temp = list(range(s.period - s.n + 1))

	# plotting logic
	#plt.title('Bollinger Bands w/ SMA and EMA')
	plt.title(s.symbol)
	plt.xlabel('Date')
	plt.ylabel('Stock Value')
	plt.plot(temp, s.SMA, label='Simple Moving Average')
	plt.plot(temp, s.EMA, label='Exponential Moving Average')
	plt.plot(temp, s.Bollinger[0], '--', label='Upper Bollinger Band')
	plt.plot(temp, s.Bollinger[1], '--', label='Lower Bollinger Band')
	plt.legend(loc='upper right')
	plt.show()
if __name__ == "__main__":
    main()

