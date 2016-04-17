# #Functions that get called from App.py
# import pymongo, smtplib, datetime, getKeys, os, time
import pymongo, smtplib, datetime, os, time
#Functions that get called from App.py
# import pymongo, datetime, getKeys, os, time
from py import output
import random
from bson.objectid import ObjectId


connection = pymongo.MongoClient ("ds019950.mlab.com", 19950)
db = connection ["heroku_rfpkgm06"]
# db.authenticate("NETS213", getKeys.getMongo())
resultList = db.resultsDB

def tmp():
    print "placeholder"

def useTime(): 
	time.sleep(10)
	return 0

def getFakeData ():
	return output.getFakeResults()

def getTurkResults(inputData):
	return output.getRealResults(inputData)

def getActualData(arg1, arg2): 
	tupleMatrix = os.system("python mturk.py arg1 arg2 50 1")
	resultsMatrix = output.getResults(output.convert(tupleMatrix))
	return resultsMatrix

def get_my_results(myID):
	return resultList.find({"user": myID})

def add_mongo_result (idNum, dscr, opt1, opt2, data):
	resultList.insert({
		"user": idNum,
		"description" : dscr,
		"option_1" : opt1, 
		"option_2": opt2,
		"html_data" : data,
		"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	})

def get_mongo_result (result_id):
	return resultList.find_one({"_id" : ObjectId(result_id)})

def get_random_ID ():
	x = random.seed()
   	x = random.getstate()
   	ID = random.random() * 1000000
   	return ID

def get_sequential_ID():
	file = open("id.txt","r")
	txt = file.read()
	file.close()
	file = open("id.txt","w")
	file.write(str(int(txt)+1))
	file.close()
	print txt
	return int(txt)
