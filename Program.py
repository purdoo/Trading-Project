import Quandl as Q
import numpy as np

import QuandlAPI as QAPI
import pytrade as pyt

# sample use of QuandlAPI library
#lastMonthClosing = Q.get("YAHOO/AAPL.6", rows=30, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")


# Use of the custom library for this project
#lastMonthClosing = QAPI.getClosing("AAPL", 30)
lastWeekClosing = QAPI.getClosing("AAPL", 15)
#print(lastMonthClosing)
print(lastWeekClosing)
avg = pyt.nDayAverage("AAPL", 7)
print(avg)

