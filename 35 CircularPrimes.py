# How many circular primes are there below one million?

import Utilities

def FindCircularPrimes():

	circPrimes = []

	primes = Utilities.LimPrimes(0, 1000000)

	for prime in primes:
		if prime in circPrimes:
			continue

		strPrime = str(prime)
		cache = []

		for i in range(len(strPrime) + 1):
			if i == len(strPrime):
				circPrimes += cache
				break

			newPrime = int(strPrime[i:] + strPrime[:i])

			if newPrime not in primes:
				break
			else:
				cache.append(newPrime)

	print(len(set(circPrimes)))
	return len(set(circPrimes))

FindCircularPrimes()
# Returns 55