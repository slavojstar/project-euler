# Find the product of the coefficients, a and b, for the quadratic expression n^2 + an + b
# that produces the maximum number of primes for consecutive values of n, starting with n=0.

from Utilities import LimPrimes, IsPrime

def FindQuadraticPrimes():
	# Check the '27 QuadraticPrimes.pdf' file to see why b needs
	# to be a large prime and, unless b = 2, a needs to be a 
	# small odd number.
	potentialBs = LimPrimes(0, 1000)[::-1]

	potentialAs = [x for x in range(-999, 1000) if x % 2 != 0]

	maxA = 0
	maxB = 0
	maxPrimes = 0


	# Try swapping these round:
	for b in potentialBs:
		for a in potentialAs:
			n = 0
			while True:
				quadratic = n ** 2 + a * n + b
				if not IsPrime(quadratic):
					break
				n += 1
			if n > maxPrimes:
				maxPrimes = n
				maxA = a
				maxB = b

	return maxA * maxB


FindQuadraticPrimes()

# Returns -59231