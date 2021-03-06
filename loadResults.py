#!/usr/bin/python

import sys
import os
import subprocess
import time
import random
from shutil import copyfile

question="Which title do you prefer?"
n = 5
a = "Placeholder"
b = "Placeholder"
t = 6

#print "hello world"
cwdPath = os.getcwd()
startPath = cwdPath + '/mturk_backend/'
print(startPath)
path = startPath + 'samples/simple_survey/'
binPath = startPath + '/bin/'

def write():
    print('Creating new text file') 
    os.chdir(path)
    fo = open('simple_survey.input', 'w+', 0)
    fo.write('question' + '\t' + 'choice1' + '\t' + 'choice2' + '\t' + 'goldStandard1' + '\t' + 'goldStandard2' + '\t' + 'assignments' + '\n' + question + '\t' + a + '\t' + b + '\t' + getGoldStandard()[0] + '\t' + getGoldStandard()[1] + '\t' + str(n*2))

    fo.close() 

def getGoldStandard():
	os.chdir(startPath)
	fo = open('goldStandard_list.csv', 'r+', 0)
	a = fo.readlines()
	line = random.randrange(0, len(a), 1)
	print "line: " + str(line)
	os.chdir(path)
	b = a[line].split(",")
	return [b[0], b[1]]

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

def moveSuccess():
	copyfile(path + 'simple_survey.success', 
		newPath + 'simple_survey.success')


def runComponents(aI,bI,tI): 
	global a 
	a = aI
	global b 
	b = bI
	global t
	t = tI
	global newPath
	newPath = path + "newDir" + str(t) +'/'
	write()
	mkNewDirs()
	run()
	moveSuccess()
