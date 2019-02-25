# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def FindDigitFifthPowers():
	# Call the sum of the digits of n to the fifth
	# powers S(n). Then we have that S(n) <= k * 9^5 where
	# k is the amount of digits of n (ceiling(log_10(n))). We
	# can look at where the graphs y = x and y = 9^5 * ceiling(log_10(x)) meet
	# to provide a reasonable upper bound to our search space.

	# Reading the graph from the file gives us 354320 as a reasonable upper bound
	resultingSum = 0

	for i in range(2, 354320):
		powerSum = 0
		iString = str(i)
		if ('5' in iString and i < 5 ** 5) or ('6' in iString and i < 6 ** 5) or ('7' in iString and i < 7 ** 5) or ('8' in iString and i < 8 ** 5) or ('9' in iString and i < 9 ** 5):
			continue
		for j in iString:
			powerSum += int(j) ** 5
		if i == powerSum:
			print(i)
			resultingSum += i

	return resultingSum

FindDigitFifthPowers()
# Returns 443839