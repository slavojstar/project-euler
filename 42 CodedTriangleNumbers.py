'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value
for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we
shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
'''

import math

def FindCodedTriangleNumbers():
	# The existence of a triangle number t means that
	# there exists an n such that t = n(n + 1) / 2 with
	# n a nonzero natural number.
	# Hence if t is a triangle number, then the equation
	# n^2 + n - 2t = 0 should have integer roots which is the
	# same as saying that (-1 ± (1 + 8t)^0.5) / 2 is an integer
	# (quadratic formula).

	words = []

	with open('42 words.txt') as wordFile:
		for line in wordFile:
			words = line.split('\",\"').copy()

	# Take off the beginning and end "s
	words[0] = words[0][1:]
	words[-1] = words[-1][:-1]

	tWords = 0
	alphaDict = {
	'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
	'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
	'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
	's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
	'y': 25, 'z': 26
	}

	for word in words:
		wordScore = 0
		for char in word:
			wordScore += alphaDict[char.lower()]
		soln = (1 + 8 * wordScore) ** (1 / 2)
		if soln % 2 == 1 and soln == math.floor(soln):
			tWords +=1

	print(tWords)
	return tWords

FindCodedTriangleNumbers()
# Returns ???

