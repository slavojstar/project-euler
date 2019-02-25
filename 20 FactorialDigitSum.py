# Find the sum of the digits in the number 100!

from math import log, pow, ceil

def FindFactorialDigitSum():
	# Create a list of the factors of 100! and 101.
	facList = list(range(1, 102))

	# Find all pairs of numbers, one with a factor of 2
	# the other with a factor of 5 and divide them each by
	# their respective factors, given that each pair of 2 and 5
	# will only contribute a 0 to the end of the factorial
	i = 0
	condition = True
	while condition:
		if i == 100:
			break
		if facList[i] % 2 == 0:
			for j in range(101):
				if j == 100:
					condition = False
					break
				if facList[j] % 5 == 0:
					facList[i] /= 2
					facList[j] /= 5
					break
		else:
			i += 1

	# Chop off the 101 from the end
	facList = facList[:-1]

	# Get rid of any 1s
	facList = [x for x in facList if x > 1]
	
	for i in range(len(facList)):
		facList[i] = int(facList[i])

	prod = 1
	for i in facList:
		prod *= i

	prod = str(prod)

	prodSum = 0

	for i in prod:
		prodSum += int(i)

	print(prodSum)
	return prodSum

FindFactorialDigitSum()
# Returns 648