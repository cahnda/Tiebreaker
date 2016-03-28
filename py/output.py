

#Maps each response (Worker ID) to a list [Int: Vote, String: Explanation]
fakeMatrix = {
	"1": [0,"I hate you"],
	"2": [0,"I love you"],
	"3": [1,"meh"]
}


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
	return [voteCountA,voteCountB,explanationsA,explanationsB]

def getFakeResults():
	return getResults(fakeMatrix)
