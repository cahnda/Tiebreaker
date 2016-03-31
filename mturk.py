#!/usr/bin/python

import sys
import os
import subprocess
import time
from shutil import copyfile

question="Which title do you prefer?"
a=str(sys.argv[1])
print a
b=str(sys.argv[2])
print b
n=int(sys.argv[3])
print n
t=int(sys.argv[4])
print t

print "hello world"
startPath = '/Users/jackcahn/Desktop/mturk_backend/'
path = startPath + 'samples/simple_survey/'
newPath = path + "newDir" + str(t) +'/'
binPath = startPath + '/bin/'

def write():
    print('Creating new text file') 

    fo = open('simple_survey.input', 'w+', 0)
    fo.write('question' + '\t' + 'choice1' + '\t' + 'choice2' + '\n' + question + '\t' + a + '\t' + b)
    fo.close()

def mkNewDirs(): 
	os.system("rm -rf " + newPath)
	os.mkdir(newPath)
	copyfile(path + 'simple_survey.properties', 
		newPath + 'simple_survey.properties')
	copyfile(path + 'simple_survey.input', 
		newPath + 'simple_survey.input')
	copyfile(path + 'simple_survey.question', 
		newPath + 'simple_survey.question')
	copyfile(path + 'getResults.sh', 
		newPath + 'getResults.sh')

def run(): 
	print binPath
	os.chdir(binPath)
	executable = "./loadHITs.sh $1 $2 $3 $4 $5 $6 $7 $8 $9 -label ../samples/simple_survey/simple_survey -input ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.input -question ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.question -properties ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.properties"
	os.system(executable)
	os.chdir(path)

def checkIfFinished():
	os.chdir(newPath)
	fo = open('simple_survey.results')
	lines = len(fo.readlines())
	print "lines: " + str(lines)
	return lines == n+1

def getResults(): 
	os.chdir(binPath)
	executable = "./getResults.sh $1 $2 $3 $4 $5 $6 $7 $8 $9 -successfile ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.success -outputfile ../samples/simple_survey/newDir" + str(t) + '/' + "simple_survey.results"
	print (executable)
	os.system(executable)
	os.chdir(path)

def moveSuccess():
	copyfile(path + 'simple_survey.success', 
		newPath + 'simple_survey.success')

def getDataStructure():
	array_of_tuples = []
	#for i in range(n-1):
	#	array_of_tuples.append((0, "not submitted yet"))

	os.chdir(newPath)
	fo = open('simple_survey.results')
	content = fo.readlines()
	cells = str(content[0]).split("\t")
	column1 = 0;
	column2 = 0;
	i = 0;
	while (column1 == 0 or column2 == 0):
		print cells[i]
		if (str(cells[i]).find("Answer.1") != -1):
			column1 = i
			print "1"
		if (str(cells[i]).find("Answer.2") != -1):
			column2 = i
			print "2"
		i = i + 1
	print "column1:" + str(column1)
	print "column2:" + str(column2)
	j = 0
	while (j < n):
		line = content[j+1].split("\t")
		item1 = line[column1].rstrip('\n')
		item2 = line[column2].rstrip('\n')
		if (item1 == ""):
			item1 = "testResponse"
		if (item2 == ""):
			item2 = "testResponse"
		array_of_tuples.append((item1,item2))
		print array_of_tuples[j]
		j = j + 1
	print array_of_tuples
	return array_of_tuples

def main():
	os.chdir(path)
	write()
	mkNewDirs()
	run()
	moveSuccess()
	getResults()
	while (not checkIfFinished()):
		time.sleep(600)
		print "waiting"
		getResults()
	print "results returned"
	dataStructure = getDataStructure()
	return dataStructure

#main()
getResults()
dataStructure = getDataStructure()
#subprocess.call(["./getResults.sh"])


#Return a table with the data
#Approve and Delete