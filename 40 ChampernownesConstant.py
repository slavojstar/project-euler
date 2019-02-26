# If dn represents the nth digit of the fractional part of Champernowne's constant,
# find the value of the following expression:

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import Utilities

def FindChampernownesConstant():

	multiplicand = 1
	for i in range(7):
		multiplicand *= Utilities.NthChampernowne(10 ** i)
	print(multiplicand)
	return multiplicand

FindChampernownesConstant()
# Returns 210