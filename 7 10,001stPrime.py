# What is the 10 001st prime number?

import math

def FindTenThousandAndFirstPrime():

	primes = []
	primes.append(2)
	primes.append(3)
	primes.append(5)

	nextSuspectedPrime = 7

	while len(primes) != 10001:
		limit = int(math.floor(math.sqrt(nextSuspectedPrime)))
		for i in range(3, limit + 3, 2):
			if nextSuspectedPrime % i == 0:
				break
			elif i == limit + 1 or i == limit + 2:
				primes.append(nextSuspectedPrime)
				print nextSuspectedPrime

		nextSuspectedPrime += 2

	print primes[len(primes) - 1]
	return primes[len(primes) - 1]

FindTenThousandAndFirstPrime()
# Returns 104743