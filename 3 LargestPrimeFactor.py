# What is the largest prime factor of the number 600851475143?

def FindLargestPrimeFactor():
	target = 600851475143
	divisor = 2

	while True:
		if target % divisor == 0 and target != divisor:
			target /= divisor
			divisor = 2
		elif target == divisor:
			break
		else:
			divisor += 1

	print divisor
	return divisor

FindLargestPrimeFactor()
# Returns 6857
