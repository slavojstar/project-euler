# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import Utilities

def FindDistinctPrimesFactors():
	i = 647

	while True:
		if len(set(Utilities.PrimeFactors(i))) != 4:
			i += 1
			continue
		elif len(set(Utilities.PrimeFactors(i + 1))) != 4:
			i += 2
			continue
		elif len(set(Utilities.PrimeFactors(i + 2))) != 4:
			i += 3
			continue
		elif len(set(Utilities.PrimeFactors(i + 3))) != 4:
			i += 4
			continue
		else:
			print(i)
			return i
			

FindDistinctPrimesFactors()
# Returns 134043