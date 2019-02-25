# What is the value of the first triangle number to have over five hundred divisors?

from Utilities import PowerSet, PrimeFactors

def FindHighlyDivisibleTriangularNumber():
	# Each triangular number can be represented in the form
	# n(n + 1) / 2 for n an integer >=1

	factors = 0
	i = 1

	while factors < 501:
		if i % 2 == 0:
			l = int(i / 2)
			k = i + 1

			primeL = PrimeFactors(l)
			primeK = PrimeFactors(k)

			primes = primeL + primeK
			factors = len(set(PowerSet(primes)))
			i += 1
		else:
			l = i
			k = int((i + 1) / 2)

			primeL = PrimeFactors(l)
			primeK = PrimeFactors(k)
			primes = primeL + primeK
			factors = len(set(PowerSet(primes)))
			i += 1

	i -= 1

	print(int(i * (i + 1) / 2))
	return int(i * (i + 1) / 2)

FindHighlyDivisibleTriangularNumber()
# Returns 76576500