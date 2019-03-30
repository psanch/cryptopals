import binascii
import codecs

from math import sqrt

# GLOBAL VARIABLES ====

test_vector = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
test_characters = 'abcdefghijklmnopqrstuvwxyz'
english_character_frequencies = {'E':0.1202,'T':0.091,'A':0.0812,'O':0.0768,'I':0.0731,'N':0.0695,'S':0.0628,'R':0.0602,'H':0.0592,'D':0.0432,'L':0.0398,'U':0.0288,'C':0.0271,'M':0.0261,'F':0.023,'Y':0.0211,'W':0.0209,'G':0.0203,'P':0.0182,'B':0.0149,'V':0.0111,'K':0.0069,'X':0.0017,'Q':0.0011,'J':0.001,'Z':0.0007}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# FUNCTION DEFINITIONS ====

def fixedXOR(p, q):
	'''
	p : str representing hex
	q : str representing hex

	r: str representing hex
	'''
	if len(p) != len(q):
		return -1
	a = int(p,16)
	b = int(q,16)
	c = hex(a^b)[2:]
	return(c)

def getDictCharacters(s):
	'''
	Creates a dictionary from all characters in s.
	Key = character, Value = Hex encoding

	s : str in ASCII

	r : dictionary
	'''
	char_list = list(s)
	char_dict = {}
	for char in char_list:
		char_dict[char] = char.encode("utf-8").hex()
	return char_dict

def extendHex(h,l):
	'''
	Make a hex encoding into length l
	'''
	tmp = ""
	for i in range(int(l)):
		tmp = tmp + h
	return tmp

def getSingleCharacterXOR(charHex, vector):
	'''
	Try a single character in an XOR fashion across a vector

	charHex : single hex character
	vector : string representing hex

	r : charHex XOR vector
	'''
	
	finalHex = extendHex(charHex, len(vector)/2 )

	res = fixedXOR(finalHex, vector)
	return res

def tryDictXOR(d,vector):
	'''
	Tries a dictionary of char's hex encoding onto a vector

	d : dictionary; setup by getDictCharacters
	vector : string to be XORd

	r : list of hex strings representing resulting XOR
	'''
	res = []
	for k,v in d.items():
		res.append(getSingleCharacterXOR(v, vector))
	return res

def singleCharCipher(test_vector):
	'''
	Get a dict. Try dict across vector. 

	r : list of ascii strings
	'''
	myDict = getDictCharacters(test_characters)

	res = tryDictXOR(myDict, test_vector)
	
	raw_ascii = []

	i = 0
	for hx in res:
		if(len(hx)%2 != 0):
			hx+='0'
		raw_ascii.append(str(binascii.unhexlify(hx), 'ascii', 'ignore'))

	return raw_ascii

def getCounts(strings):
	counts = []
	for string in strings:
		tmp = getCharCounts(string)
		counts.append(tmp)
	return counts

def getCharCounts(s):
	counts = {}
	for c in s:
		char = str(c).upper()
		counts[char] = counts.get(char, 0) + 1
	return counts

def getSumDictValues(dictList):
	tmp = []
	for d in dictList:
		tmp.append(sum(d.values()))
	return tmp

def stripNullBytes(inputList):
	res = []

	for s in inputList:

		x = s
		res.append(x)

	return res

def getFrequencies(dictionaryList, sumList):

	if(len(dictionaryList) != len(sumList)):
		return -1

	l = len(dictionaryList)

	res = []

	#for every dictionary
	for i in range(l):
		tmp = {}
		
		#for every key, value pair
		for k,v in dictionaryList[i].items():
			#compute frequency
			tmp[k] = float((dictionaryList[i][k])) / float(sumList[i])
			
		#create frequencyList
		res.append(tmp)

	return res

def getEuclidianDistance(v1,v2):
	if(len(v1) != len(v2)):
		return -1

	tmpAdd = 0
	for i in range(len(v1)):
		tmpSub = ((v1[i]-v2[i])**2)
		tmpAdd += tmpSub

	return sqrt(tmpAdd)

def getDistanceList(myFreq, englishFreq):
	'''
	myFreq is a list of 26 dictionaries (one for each character attempted) containing the frequencies for those 
	'''

	distList = []
	#for each dictionary in list of dicts
	for d in myFreq:
		tmp = []
		#turn it into a list of frequencies organized in alphabetical order
		for char in alphabet:
			charFreq = d.get(char,0)
			tmp.append(charFreq)
		distList.append(tmp)

	englishList = []
	for char in alphabet:
		englishList.append(englishFreq.get(char,0))

	eucDistances = []
	for sublist in distList:
		eucDistances.append(getEuclidianDistance(sublist,englishList))

	return eucDistances

def getSortedIndicesList(distList):
	sortingList = []
	for i,x in enumerate(distList):
		sortingList.append((i,x))

	sortingList.sort(key=lambda tup: tup[1])
	
	return sortingList

def alphabetCharXORstring(testVector, topResults):
	'''
	str: testVector is a string (ascii) over which all (26) possible english characters will be XOR'd. 
	The resulting plaintext will be ranked with respect to its character frequency's euclidean distance from expected frequency values for the english language.
	int: topResults determines how many (the top n) results will be output.
	'''

	#get a list of ascii strings that represent CHAR XOR vector
	resultsList = singleCharCipher(testVector)

	cleanResultsList = stripNullBytes(resultsList)

	#get a list of dictionaries with the letter counts in each of the above strings
	countsDictionaryList = getCounts(cleanResultsList)

	#get a list of ints that represent the lengths of the above strings
	sumDictValuesList = getSumDictValues(countsDictionaryList)

	#get a list of character frequencies for each of the above strings
	frequencyList = getFrequencies(countsDictionaryList, sumDictValuesList)

	distanceList = getDistanceList(frequencyList, english_character_frequencies)

	indicesList = getSortedIndicesList(distanceList)

	likelyEnglishList = []
	for i in range(topResults):
		likelyEnglishList.append(   (   str(cleanResultsList[indicesList[i][0]]),  alphabet[indicesList[i][0]] , indicesList[i][1]  )  )
	return likelyEnglishList


# ==================================
# Above this point challenge 3 =====
# ==================================

def resultPrint(l):
	for t in l:
		print('\nMessage =',t[0])
		print('Frequency = ',t[2],'Character = ',t[1])

def parseStringsFromFile(filename):
	f = open(filename,'r')
	lines = f.readlines()
	cleanLines = []
	for line in lines:
		cleanLines.append(line.strip())
	return cleanLines


def decryptTheStringList(filename, topResults):

	theStringList = parseStringsFromFile(filename)

	possiblyEnglish = []
	for string in theStringList:
		for sublist in alphabetCharXORstring(string,topResults):
			possiblyEnglish.append(sublist)

	possiblyEnglish.sort(key= lambda tup: tup[2], reverse=True)
	return possiblyEnglish

resultPrint(decryptTheStringList('60characterStrings.txt', 10))
