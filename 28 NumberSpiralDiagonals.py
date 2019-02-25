# What is the sum of the numbers on the diagonals in a 1001 by 1001 number spiral?

from math import floor

def FindNumberSpiralDiagonals():
	# The amount of numbers in the diagonals is 1000 * 2 + 1 = 2001
	# The increasing sequence formed by numbers of the diagonal
	# is as follows:
	# 1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49, 57
	# with the sequence of differences as follows:
	# 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 8
	# So we just need to sum 2001 of these terms

	term = 1
	termSum = 1

	for i in range(2000): 
		term += (floor(i / 4) + 1) * 2
		termSum += term
	print(termSum)
	return termSum

FindNumberSpiralDiagonals()

# Returns 