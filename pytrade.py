# PyTrade Library
import Quandl as Q
import numpy as np
import QuandlAPI as QAPI

def nDayAverage(stockname, n, dec=2):
	pull = QAPI.getClosing(stockname, n)
	return (round(np.mean(pull),dec))

