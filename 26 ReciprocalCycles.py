# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

def FindReciprocalCycles():

	seqLength = 0
	num = 0

	for i in range(1000, 1, -1):
		if seqLength >= i:
			break

		remainders = []
		value = 1
		position = 0

		while remainders[value] == 0 and value != 0:
			remainders[value] = position
			value *= 10
			value = value % i
			position += 1

		if position - remainders[value] > seqLength:
			num = i
			seqLength = position - remainders[value]

	print(num)
	return num

FindReciprocalCycles()
# Returns 983