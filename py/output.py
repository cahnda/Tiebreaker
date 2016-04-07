

#Maps each response (Worker ID) to a list [Int: Vote, String: Explanation]
fakeMatrix = {
	"1": [0,"Response1"],
	"2": [0,"Response2"],
	"3": [0,"Response3"],
	"4": [0,"Response4"],
	"5": [0,"Response5"],
	"6": [0,"Response6"]
}

sampleResults = [(0,"Response1"),(0,"Response2"),(0,"Response3"),(0,"Response4"),(0,"Response5"),(0,"Response6")]

def getResults(resultsMatrix):
	voteCountA = 0
	voteCountB = 0
	explanationsA = []
	explanationsB = []
	for val in resultsMatrix:
		lst = resultsMatrix.get(val)
		if (lst[0] == 0):
			voteCountA = voteCountA + 1
			explanationsA.append(lst[1])
		else: 
			voteCountB = voteCountB + 1
			explanationsB.append(lst[1])
	#while (len (explanationsA) > len (explanationsB)):
		#explanationsB.append(" ")
	#while (len (explanationsB) > len (explanationsA)):
		#explanationsA.append(" ")
	return [voteCountA,voteCountB,explanationsA,explanationsB]

def convert(tupleMatrix):
	num = 0
	outputMatrix = {}
	for tpl in tupleMatrix:
		outputMatrix[str(num)] = [tpl[0],tpl[1]]
		num = num + 1
	return outputMatrix

def getFakeResults():
	return getResults(convert(sampleResults))
