import sys
import os
import subprocess
import time
import random
import csv ,operator
from shutil import copyfile

t = 0
n = 0
max_t = 0
cwdPath = os.getcwd()
startPath = cwdPath + '/mturk_backend_brainstormit/'
path = startPath + 'samples/simple_survey/'
newPath = path + "newDir" + str(t) +'/'
binPath = startPath + '/bin/'

def checkIfFinished():
	os.chdir(newPath)
	fo = open('simple_survey.results')
	a = fo.readlines()
	lines = len(a)
	print "lines :" + str(lines)
	print n+1
	return lines == n+1

def getResults(): 
	os.chdir(binPath)
	print ("GETTING RESULTS FOR T=" + str(t))
	executable = "./getResults.sh $1 $2 $3 $4 $5 $6 $7 $8 $9 -successfile ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.success -outputfile ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.results"
	print (executable)
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
	column3 = 0;
	i = 0;
	while (column1 == 0 or column2 == 0 or column3 == 0):
		if (str(cells[i]).find("Answer.1") != -1):
			column1 = i
		if (str(cells[i]).find("Answer.5") != -1):
			column2 = i
		if (str(cells[i]).find("Answer.6") != -1):
			column3 = i
		i = i + 1
	j = 0
	while (j < 10):
		print "REACHED"
		print j
		print len(array_of_tuples)
		try: 
			line = content[j+1].split("\t")
			item1 = line[column1].rstrip('\n')
			print item1
			item2 = line[column2].rstrip('\n')
			print item2
			item3 = line[column3].rstrip('\n')
			print item3
			array_of_tuples.append(item1)
			array_of_tuples.append(item2)
			array_of_tuples.append(item3)
			j = j + 1
		except: 
			break

		if (item1 == ""):
			item1 = "Placeholder"
		if (item2 == ""):
			item2 = "Placeholder"

	print "PRINTING ARRAY"
	print array_of_tuples
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
	print "N: " + b[x]
	return int(b[x])

def getNextArray():
	try:
		os.chdir(newPath)
		print "found path"
	except OSError: 
		print "didn't find path"
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
	#if (checkIfFinished() == True):
	#try:
	#	print "TRUE"
	#	dataStructure = getDataStructure()
	#	return (1, dataStructure)
	#except:
	#	dataStructure = getDataStructure()
	#	return (1, dataStructure)
	#else:
	#	try: 
	#		dataStructure = getDataStructure()
	#		print "PARTIAL DATA STUCTURE"
	#		return (1, dataStructure)
	#	except: 
	#	return (-1, [])

	#try: 
	#	dataStructure = getDataStructure()
	#	print "PARTIAL DATA STUCTURE"
	#	return (1, dataStructure)		
	#except: 
	#	return (-1, [])

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
		print "Values:" + str(len(values))
		for item in values:
			print item

def main():
	dictArrays = resultsComponents()
	printDict(dictArrays)
	global t
	t = 0
	return dictArrays