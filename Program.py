import Quandl as Q
import numpy as np
import QuandlAPI as QAPI
import pytrade as pyt


# sample use of QuandlAPI library
#lastMonthClosing = Q.get("YAHOO/AAPL.6", rows=30, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
#print(lastMonthClosing.index.tolist())

# Use of BollingerBands function in pytrade


"""
s = pyt.Stock('Apple', 'AAPL')
print(s.data)
print(s.nDayAverage(15))
"""