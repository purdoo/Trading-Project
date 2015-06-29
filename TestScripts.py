import Quandl as Q
import numpy as np
import pytrade as pyt
"""
Moving Average and EMA Test Case

Example Calculations:
http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages

We want to make sure our results match up with this example when we have the same closing price data

"""

testclosing = [22.17,22.40,23.10,22.68,23.33,23.10,23.19,23.65,23.87,23.82,23.63,23.96,23.83,23.75,24.05,
				23.36,22.61,22.38,22.39,22.15,22.29,22.24,22.43,22.23,22.13,22.18,22.17,22.08,22.19,22.27]
#print(len(testclosing))

s = pyt.Stock('Apple', 'AAPL', 30, testclosing)
print(s.getMovingAverage(10, 30, dec=2))
print(s.getEMA(10, 30))
#s.getEMA(10, 30)