# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

import Utilities

def FindTruncatablePrimes():
	primes = []
	prime = 11
	strPrime = str(prime)

	while len(primes) < 11:
		if ('2' in strPrime or '4' in strPrime or '6' in strPrime
			or '8' in strPrime or '0' in strPrime):
			continue
		if IsTruncatedPrime(prime):
			primes.append(prime)

		prime += 2

	print(primes)
	print(sum(primes))
	return sum(primes)

def IsTruncatedPrime(p):
	''' Checks whether a prime p is a truncatable prime. '''
	if not Utilities.IsPrime(p) or p == 2 or p == 3 or p == 5 or p == 7:
		return False

	strPrime = str(p)

	for i in range(1, len(strPrime)):
		leftPrime = int(strPrime[i:])
		rightPrime = int(strPrime[:i])

		if Utilities.IsPrime(leftPrime) and Utilities.IsPrime(rightPrime):
			continue
		else:
			return False

	return True

FindTruncatablePrimes()
# Returns 748317