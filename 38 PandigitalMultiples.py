# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
#the concatenated product of an integer with (1,2, ... , n) where n > 1?

import Utilities

def FindPandigitalMultiples():
	# Lets think about reducing the search space:
	# The number can't have any duplicates, and it can't
	# have a 0 in it.

	largestPan = 0
	largestMultiplier = 0

	for i in range(1, 9877):

		strI = str(i)

		# Check for duplicates
		if len(set(strI)) != len(strI):
			continue
		if '0' in strI:
			continue

		finString = ''
		multiplicand = 1

		# The possible pandigital cannot be more than 9 digits
		# so the multiplicand can't go higher than 9.
		while len(finString) != 9 and multiplicand < 10:
			stringToCat = str(multiplicand * i)
			if '0' in stringToCat:
				break
			if len(set(stringToCat)) != len(stringToCat):
				break
			finString += stringToCat
			multiplicand += 1

		if not len(finString) == 9 or not Utilities.IsPandigital(finString, 9):
			continue
		elif int(finString) > largestPan:
			largestPan = int(finString)
			largestMultiplier = i

	print(largestPan)
	print(largestMultiplier)
	return largestPan

FindPandigitalMultiples()
# Returns ???