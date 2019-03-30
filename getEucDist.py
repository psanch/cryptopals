def getEuclidianDistance(v1,v2):
	if(len(v1) != len(v2)):
		return -1

	tmpAdd = 0
	for i in range(len(v1)):
		tmpSub = ((v1-v2)**2)
		tmpAdd += tmpSub

	return sqrt(tmpAdd)


