from math import sqrt

def getEuclidianDistance(v1,v2):
	if(len(v1) != len(v2)):
		return -1

	tmpAdd = 0
	for i in range(len(v1)):
		tmpSub = ((v1[i]-v2[i])**2)
		tmpAdd += tmpSub

	return sqrt(tmpAdd)

print(getEuclidianDistance([1,1,1], [0,0,0]))


