# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# (not including 1 and 2)

import math

def FindDigitfactorials():
	# There must be a point at which it is impossible to add
	# up the factorials of the digits of a number, to get that
	# number. Let's find out where the limit lies.

	# See the file "34 DigitFactorialGraphUpperBound.pdf" for an explanation
	# of why we only need to search up to 2.5402 x 10^6
	resultingSum = 0

	for i in range(3, 2540200):
		facSum = 0
		iString = str(i)
		# if '7' is one of the digits, then the number will have to be
		# at least 7!. Likewise with 8 and 9.
		if ('7' in iString and i < math.factorial(7)) or ('8' in iString and i < math.factorial(8)) or ('9' in iString and i < math.factorial(9)):
			continue
		for j in range(len(iString)):
			facSum += math.factorial(int(iString[j]))
		if i == facSum:
			resultingSum += facSum
	print(resultingSum)
	return resultingSum;


FindDigitfactorials()
# Returns 40730