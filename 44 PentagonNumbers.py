# Find the pair of pentagonal numbers, Pj and Pk, for which their sum
# and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

import math

def FindPentagonNumbers():
	penPairs = []
	for i in range(1, 10000):
		for j in range(i + 1, 10000):
			inspect1 = math.sqrt(1 + 12 * (3 * (j ** 2 + i ** 2) - (j + i)))
			inspect2 = math.sqrt(1 + 12 * (j - i) * (3 * (j + i) - 1))
			if (inspect1 % 2 == 1 and inspect2 % 2 == 1 and\
				inspect1 == math.floor(inspect1) and inspect2 == math.floor(inspect2)):
				penPairs.append((i, j, int((j - i) * (3 * (j + i) - 1) / 2)))
	print(penPairs)
	return 0

FindPentagonNumbers()
# Returns ????