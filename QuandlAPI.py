import Quandl as Q
import numpy as np
# this file should contain the methods for requesting data
# we should attempt to keep the main program as clean as possible



def getClosing(stockname, n):
	searchstring = "YAHOO/" + stockname + ".6"
	# returns a Pandas series
	pull = Q.get(searchstring, rows=n, sort_order='desc', authtoken="QyJB1_5vMdTh-GSMWar7")
	return formatToList(pull.values)



# not currently being used
def formatToList(listOfLists):
	#return listOfLists.tolist()
	return listOfLists