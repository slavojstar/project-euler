# Work out the first ten digits of the sum of the one-hundred 50-digit numbers in the file
# LargeSum.txt

import Utilities

def FindLargeSum():

	largeSum = '0'

	with open('LargeSum.txt') as sumFile:
		for line in sumFile:
			# Snip off end of line character for all but the last line
			if line != '53503534226472524250874054075591789781264330331690':
				line = line[:-1]
			largeSum = Utilities.LargeSum(largeSum, line)

	largeSumStr = str(largeSum)

	print(largeSum)
	return largeSum

FindLargeSum()
# Returns ????