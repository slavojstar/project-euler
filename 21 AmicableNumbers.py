# Evaluate the sum of all the amicable numbers under 10000.

from Utilities import IsAmicable

def FindAmicableNumbers():
	amiNums = []
	for i in range(2, 10000):
		if i in amiNums:
			continue
		amiTuple = IsAmicable(i)
		if amiTuple[0]:
			amiNums.append(i)
			amiNums.append(amiTuple[1])

	print(sum(amiNums))
	return sum(amiNums)

FindAmicableNumbers()
# Returns 31626