#!/usr/bin/python

import sys
import os
import subprocess
import time
import random
from shutil import copyfile

question = ""
t = 6
newPath = ""
cwdPath = os.getcwd()
startPath = cwdPath + '/mturk_backend_brainstormit/'
path = startPath + 'samples/simple_survey/'
binPath = startPath + '/bin/'
n = 10

def write():
    print('Creating new text file') 
    os.chdir(path)
    fo = open('simple_survey.input', 'w+', 0)
    global quesiton
    fo.write('question' + '\t' + 'assignments' + '\n' + question + '\t' + str(n))
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

def moveSuccess():
	copyfile(path + 'simple_survey.success', 
		newPath + 'simple_survey.success')


def runComponents(qI,tI): 
	global question
	question = qI
	global t
	t = tI
	global newPath
	newPath = path + "newDir" + str(t) +'/'
	write()
	mkNewDirs()
	run()
	moveSuccess()

