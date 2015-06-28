# PyTrade Library
import Quandl as Q
import numpy as np
import QuandlAPI as QAPI

class Stock:
	def __init__(self, name, symbol, n = 90):
		self.name = name
		self.symbol = symbol
		self.closing = QAPI.getClosing(symbol, n)
		# sanity check
		self.data = Q.get("YAHOO/AAPL", rows=30, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
	
	def nDayAverage(self, n, dec=2):
		values = self.closing[:n]
		return (round(np.mean(values),dec))

	def getMovingAverage(self, n, days, dec=2):
		movingAverages = []
		if(n > days):
			print("n cannot be greater than the number of days")
			return movingAverages
		count = (days - n) + 1
		for i in range(count):
			sample = self.closing[i:i+n]
			print(sample)
		return movingAverages

""" Test Area - For when I don't want to put crap in the Program """
s = Stock('Apple', 'AAPL')
print(s.data)
s.getMovingAverage(10,30)

