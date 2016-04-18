#Functions that get called from App.py
import pymongo, getKeys, datetime, os, time
from py import output
import random
from bson.objectid import ObjectId


connection = pymongo.MongoClient ("ds019950.mlab.com", 19950)
db = connection ["heroku_rfpkgm06"]
db.authenticate("NETS213", getKeys.getMongo())
resultList = db.resultsDB
count = db.count

def tmp():
    print "placeholder"

def useTime(): 
	time.sleep(10)
	return 0

def getFakeData ():
	return output.getFakeResults()

def getTurkResults(inputData,input1,input2):
	return output.getRealResults(inputData,input1,input2)

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
	doc = count.find_one({"_id" : ObjectId("57142510e4b065a8c4d72ab9")})
	txt = doc["value"]
	count.update({"_id" : ObjectId("57142510e4b065a8c4d72ab9")},{"value":txt +1})
	count.update
	print txt
	return txt
