# What is the total of all the name scores in the file names.txt?

def FindNamesScores():

	nameList = []

	with open("22 Names.txt") as names:
		for line in names:
			lineList = line.split('\",\"')
			nameList += lineList

	nameList[0] = nameList[0][1:]
	nameList[len(nameList) - 1] = nameList[len(nameList) - 1][:-1]
	nameList.sort()

	alphaScoreDict = {
	'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
	'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
	'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
	's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
	'y': 25, 'z': 26
	}

	score = 0

	for i in range(len(nameList)):
		nameScore = 0
		for letter in nameList[i]:
			nameScore += alphaScoreDict[letter.lower()]
		score += nameScore * (i + 1)

	print(score)
	return score

FindNamesScores()
# Returns 871198282