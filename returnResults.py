#!/usr/bin/python

import sys
import os
import subprocess
import time
import random
from shutil import copyfile

t = 0
n = 0
max_t = 0

startPath = '/Users/cahnda/Dropbox/Apps/Tiebreaker/mturk_backend/'
path = startPath + 'samples/simple_survey/'
newPath = path + "newDir" + str(t) +'/'
binPath = startPath + '/bin/'

def checkIfFinished():
	os.chdir(newPath)
	fo = open('simple_survey.results')
	a = fo.readlines()
	lines = len(a)
	#print lines
	#print n+1
	return lines == n+1

def getResults(): 
	os.chdir(binPath)
	executable = "./getResults.sh $1 $2 $3 $4 $5 $6 $7 $8 $9 -successfile ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.success -outputfile ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.results"
	#print (executable)
	os.system(executable)
	os.chdir(path)

def getDataStructure():
	array_of_tuples = []

	os.chdir(newPath)
	fo = open('simple_survey.results')
	content = fo.readlines()
	cells = str(content[0]).split("\t")
	column1 = 0;
	column2 = 0;
	i = 0;
	while (column1 == 0 or column2 == 0):
		if (str(cells[i]).find("Answer.1") != -1):
			column1 = i
		if (str(cells[i]).find("Answer.2") != -1):
			column2 = i
		i = i + 1
	j = 0
	while (j < n):
		try:
			line = content[j+1].split("\t")
			item1 = line[column1].rstrip('\n')
			item2 = line[column2].rstrip('\n')
			if (item1 == ""):
				item1 = "testResponse"
			if (item2 == ""):
				item2 = "testResponse"
			array_of_tuples.append((item1,item2))
			#print array_of_tuples[j]
			j = j + 1
		except: 
			break;
	#print array_of_tuples
	return array_of_tuples

def readN():
	os.chdir(newPath)
	fo = open('simple_survey.input')
	y = fo.readlines()
	a = y[0]
	b = a.split('\t')
	x = 0
	while ((b[x])[0:11] != "assignments"):
		x = x + 1
	a = y[1]
	b = a.split('\t')	
	return int(b[x])

def getNextArray():
	try:
		os.chdir(newPath)
	except OSError: 
		global max_t
		max_t = t-1
		return (-1, [])
	getResults()
	global n
	n = readN()
	dataStructure = []
	if (checkIfFinished() == True):
		#print "TRUE"
		dataStructure = getDataStructure()
		return (1, dataStructure)
	else:
		try: 
			dataStructure = getDataStructure()
			print "PARTIAL DATA STUCTURE"
			return (1, dataStructure)
		except: 
			return (1, [])

def resultsComponents():
	dictArrays = {}
	global t
	while (t != -1):
		print str(t) + " MY T VALUE"
		global newPath
		newPath = path + "newDir" + str(t) +'/'
		(newT, arr) = getNextArray()
		if (newT == 1):
			dictArrays[str(t)] = arr
			t = t + 1
		if (newT == -1):
			t = -1
			break;
		#print newT
		#print arr
	return dictArrays

def printDict(dictArrays):
	x = 0
	for (key, values) in dictArrays.items():
		print "Key: " + str(key)
		for (a, b) in values:
			print "Value: " + a + '\t' + b


def main():
	print "REACHED"
	dictArrays = resultsComponents()
	printDict(dictArrays)
	global t
	t = 0
	return dictArrays