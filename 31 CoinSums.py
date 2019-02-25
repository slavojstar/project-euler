# How many different ways can £2 be made using any number of coins?

from Utilities import NumberSums

def FindCoinSums():
	print NumberSums(200, 200, [1, 2, 5, 10, 20, 50, 100, 200])
	return NumberSums(200, 200, [1, 2, 5, 10, 20, 50, 100, 200])

FindCoinSums()
# returns 73682

