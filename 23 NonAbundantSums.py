# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from Utilities import FactorsOf, IsPrime

def FindNonAbundantSums():
	# By mathematical analysis, it can be shown that all integers greater than 28123
	# can be written as the sum of two abundant numbers.
	abundance = []
	for i in range(1, 28124):
		if IsPrime(i) or (i % 2 == 0 and IsPrime(int(i / 2))):
			continue
		if i % 3 == 0 and IsPrime(int(i / 3)) and i > 6:
			continue
		factors = FactorsOf(i)
		factors.remove(i)
		if sum(factors) > i:
			abundance.append(i)

	# If n is an abundant number, then so is kn, where k 
	# is a sufficiently small integer that kn < 28123

	# Make a list of numbers which are potentially impossible
	# to make as the sum of 2 abundant numbers
	nums = list(range(1, 28124))

	# Remove all elements from nums that are a
	# multiple of an abundant number
	for i in abundance:
		if i * 2 > 28123:
			break
		else:
			j = 2
			while i * j <= 28123:
				if i * j in nums:
					nums.remove(i * j)
				j += 1

	for i in range(len(abundance)):
		iBun = abundance[i]
		for j in range(i, len(abundance)):
			jBun = abundance[j]
			sumBun = iBun + jBun
			if sumBun > 28123:
				break
			elif sumBun not in nums:
				continue
			else:
				nums.remove(sumBun)

	print(sum(nums))
	return sum(nums)

FindNonAbundantSums()
# Returns 4179871






