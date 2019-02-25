# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

def FindPrimeFactors(n):
	primes = [2, 3, 5, 7, 11, 13, 17, 19]
	factors = []

	while n != 1:
		for p in primes:
			if n % p == 0:
				factors.append(p)
				n /= p
				break

	return factors

def FindSmallestMultiple():
	factors = []

	for i in range(2, 21):
		# Find everything in the set of prime factors of i, that
		# isn't already in the set of factors (i.e. set complement
		# with duplicates)
		complement = FindPrimeFactors(i)

		for factor in factors:
			if factor in complement:
				complement.remove(factor)

		factors.extend(complement)

	result = 1

	for n in factors:
		result *= n

	print result
	return result


FindSmallestMultiple()
# Returns 232792560