# What is the first value which can be written as the sum of primes in over five thousand different ways?

from Utilities import PrimeSumUnderK

def FindPrimeSummations():
	primeSum = 0
	i = 2

	while True:
		if PrimeSumUnderK(i, i) >= 5000:
			break
		else:
			i += 1

	print i
	return i


FindPrimeSummations()
# Returns 71