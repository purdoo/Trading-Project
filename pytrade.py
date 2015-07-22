# PyTrade Library
import Quandl as Q
import numpy as np
import QuandlAPI as QAPI
import pandas as pd
#import TestScripts as test
import matplotlib.pyplot as plt
import pymath as pm

""" Bollinger Bands Class """
class Stock:
	def __init__(self, name, symbol, n = 10, period = 30, testclosing = []):
		self.name = name
		self.symbol = symbol
		self.n = n
		self.period = period
		self.closing = QAPI.getClosing(symbol, period)
		self.SMA = pm.getSMA(self.closing, n, period)
		self.EMA = pm.getEMA(self.closing, n, period)
		self.Bollinger = self.getBollingerBands()

		# sanity check
		self.data = Q.get("YAHOO/AAPL", rows=period, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
		self.dates = pd.to_datetime(self.data.index[0:period-n+1], unit='D').values[::-1]
		self.testclosing = testclosing


	def nDayAverage(self, n, dec=2):
		values = self.closing[:n]
		return (round(np.mean(values),dec))

	def getBollingerBands(self):
		stdev, upperBand, lowerBand = [], [], []
		closing = self.closing[0:self.period]
		count = (self.period - self.n) + 1
		for i in range(count):
			sample = self.closing[i:(i+self.n)]
			stdev.append(np.std(sample))
			upperBand.append(self.SMA[-(i+1)] + (1*np.std(sample)))
			lowerBand.append(self.SMA[-(i+1)] - (1*np.std(sample)))
		return (upperBand[::-1], lowerBand[::-1])

""" End Bolling Bands Class """

class Delta:
	def __init__(self, name, symbol, period = 30):
		self.period = period
		self.closing = QAPI.getClosing(symbol, period)
		self.delta = self.getDelta()
		self.symbol = symbol
		self.data = Q.get("YAHOO/AAPL", rows=period, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
		self.dates = pd.to_datetime(self.data.index[0:period-1], unit='D').values[::-1]
	def getDelta(self):
		deltas = []
		for i in range(self.period - 1):
			#print(self.closing[-(i+1)])
			delta = self.closing[-(i+1)] - self.closing[-(i+2)] 
			deltas.append(-(float(delta)))
		return deltas


""" *******PLOTTING FUNCTIONS******** """
""" Bollinger Bands Plotting Function """
def bollinger(symbol, n = 10, period = 30):
	s = Stock('Name', symbol, n, period)
	plt.title(s.symbol)
	plt.xlabel('Date')
	plt.ylabel('Stock Value')
	plt.plot_date(s.dates, s.SMA, '-', label='Simple Moving Average')
	plt.plot_date(s.dates, s.EMA, '-', label='Exponential Moving Average')
	plt.plot_date(s.dates, s.Bollinger[0], '--', label='Upper Bollinger Band')
	plt.plot_date(s.dates, s.Bollinger[1], '--', label='Lower Bollinger Band')
	plt.legend(loc='upper right')
	plt.show()
	return 0


""" Change in Closing Price Plotting Function """
def delta(symbol, period = 30):
	s = Delta('Name', symbol, period)
	print(len(s.delta))
	plt.title(s.symbol)
	plt.xlabel('Date')
	plt.ylabel('Change')
	plt.bar(s.dates, s.delta)
	plt.show()





""" Test Area - For when I don't want to put crap in the Program """
def main():
	pass
if __name__ == "__main__":
    main()

