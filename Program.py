import Quandl as Q
import numpy as N
import pytrade # this is our library, must be in same directory


lastMonthClosing = Q.get("YAHOO/AAPL.6", rows=30, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
valueList = lastMonthClosing.values
print(max(valueList))
for value in valueList:
    print(value)


