#Functions that get called from App.py
import time
import os
from py import output


def tmp():
    print "placeholder"

def useTime(): 
	time.sleep(5)
	return 0

def getFakeData ():
	return output.getFakeResults()

def getActualData(arg1, arg2): 
	tupleMatrix = os.system("python mturk.py arg1 arg2 50 1")
	resultsMatrix = output.getResults(output.convert(tupleMatrix))
	return resultsMatrix