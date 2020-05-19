# Which starting number, under one million, produces
# the longest Collatz chain?

def CollatzSequence(n):
	''' Returns a list of a Collatz sequence starting at n'''
	sequence = []
	sequence.append(n)

	currentNumber = n

	while currentNumber != 1:
		if currentNumber % 2 == 0:
			currentNumber /= 2
			sequence.append(currentNumber)

		else:
			currentNumber = 3 * currentNumber + 1
			sequence.append(currentNumber)

	return sequence

def FindLongestCollatz():
	# Dictionary where the keys are the numbers up to 1,000,000
	# and the values are the length of the Collatz sequences.
	chainDict = {}

	chainDict.update({1: 1})

	# Now to find the length of Collatz sequences of numbers
	# up to and including 1,000,000
	for i in range(2, 1000001):
		# Some numbers will already be included in chainDict because
		# they are in the chains of previous numbers.
		if i in chainDict:
			continue

		# Now we add numbers, and the length of their chains, into
		# the chainDict
		sequence = CollatzSequence(i)
		length = len(sequence)

		antiIndex = 0
		for item in sequence:
			# Check for sequences colliding
			if int(item) in chainDict:
				break

			chainDict.update({int(item): length - antiIndex})
			antiIndex += 1

	maxLength = 0
	maxNumber = 0

	for key in chainDict:
		if chainDict[key] > maxLength:
			maxLength = chainDict[key]
			maxNumber = key

	print maxNumber
	return maxNumber

FindLongestCollatz()
# Returns 837799
