# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import Utilities

def FindSelfPowers():
	powerList = list(range(1, 1001))
	lastPowerList = []

	for i in powerList:
		lastPowerList.append(Utilities.LastDigsPower(i, i, 10))

	grandSumStr = str(Utilities.LastDigsSum(lastPowerList, 10))
	finalAns = int(grandSumStr[len(grandSumStr) - 10:])
	print(finalAns)
	return finalAns

FindSelfPowers()
# Returns 9110846700