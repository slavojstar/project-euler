# What is the largest n-digit pandigital prime that exists?

import Utilities

def FindPandigitalPrime():
	# It's not going to be pandigital in '1', '12', '123'
	# '12345', '123456', '12345678', or '123456789' because
	# they are all either 1 or a multiple of 3.
	# So we're looking for a permutation of '1234'

	biggest = 0
	for perm in Utilities.Permute('1234'):
		intPerm = int(perm)
		if intPerm > biggest and Utilities.IsPrime(intPerm):
			biggest = intPerm

	for perm in Utilities.Permute('1234567'):
		intPerm = int(perm)
		if intPerm > biggest and Utilities.IsPrime(intPerm):
			biggest = intPerm


	print(biggest)
	return(biggest)

FindPandigitalPrime()
# Returns ???
