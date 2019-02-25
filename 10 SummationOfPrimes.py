#Find the sum of all the primes below two million.

import math

def FindSummationOfPrimes():
	limit = 2000000
	searchLimit = int(math.floor(math.sqrt(limit)))

	# The following represents a boolean list, where each value
	# corresponds to the primality of the index (true if compount
	# false if prime)
	sieve = [False] * (limit + 1)

	# 0 is not prime so:
	sieve[0] = True

	# Starting from the boolean corresponding to 4, mark all
	# evens as compound
	for i in range(4, limit + 1, 2):
		sieve[i] = True

	# Now look for the false values under the searchLimit, which should
	# be primes p, and make true all those odd multiples of it
	# from p^2 to the limit (starting at 3 because 2 is prime)
	for i in range(3, searchLimit + 1, 2):
		if not sieve[i]:
			for j in range(int(math.pow(i, 2)), limit + 1, 2 * i):
				sieve[j] = True

	primeSum = 0

	for i in range(2, limit + 1):
		if not sieve[i]:
			primeSum += i

	print primeSum
	return primeSum

FindSummationOfPrimes()
# Returns 142913828922
