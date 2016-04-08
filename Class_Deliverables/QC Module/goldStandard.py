def getGoldStandard():
	os.chdir(startPath)
	fo = open('goldStandard_list.csv', 'r+', 0)
	a = fo.readlines()
	line = random.randrange(0, len(a), 1)
	print "line: " + str(line)
	os.chdir(path)
	b = a[line].split(",")
	return [b[0], b[1]]