# Work out the first ten digits of the sum of the one-hundred 50-digit numbers in the file
# LargeSum.txt

import Utilities

def FindLargeSum():

	largeSum = '0'

	with open('LargeSum.txt') as sumFile:
		for line in sumFile:
			# Snip off end of line character
			line = line[:-1]
			largeSum = Utilities.LargeSum(largeSum, line)

	largeSumStr = str(largeSum)

	print(largeSum)
	return largeSum

FindLargeSum()
# Returns ????