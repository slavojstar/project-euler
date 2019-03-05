# What is the smallest odd composite that cannot be written
# as the sum of a prime and twice a square?

import Utilities
import math

def FindGoldbachsOtherConjecture():
	# Search space is odd composites:
	nextSuspect = 35
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

	while True:
		if Utilities.IsPrime(nextSuspect):
			primes.append(nextSuspect)
			nextSuspect += 2
			continue
		else:
			i = 0
			while True:
				if i == len(primes):
					print(nextSuspect)
					return nextSuspect
				else:
					checkSquare = math.sqrt((nextSuspect - primes[i]) / 2)
					if checkSquare == math.floor(checkSquare):
						break
					else:
						i += 1
			nextSuspect += 2
	return 0

FindGoldbachsOtherConjecture()
# Returns 5777