# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?
from functools import reduce


def FindLargestProductInASeries():

	numberString = ""

	numberString += "73167176531330624919225119674426574742355349194934"
	numberString += "96983520312774506326239578318016984801869478851843"
	numberString += "85861560789112949495459501737958331952853208805511"
	numberString += "12540698747158523863050715693290963295227443043557"
	numberString += "66896648950445244523161731856403098711121722383113"
	numberString += "62229893423380308135336276614282806444486645238749"
	numberString += "30358907296290491560440772390713810515859307960866"
	numberString += "70172427121883998797908792274921901699720888093776"
	numberString += "65727333001053367881220235421809751254540594752243"
	numberString += "52584907711670556013604839586446706324415722155397"
	numberString += "53697817977846174064955149290862569321978468622482"
	numberString += "83972241375657056057490261407972968652414535100474"
	numberString += "82166370484403199890008895243450658541227588666881"
	numberString += "16427171479924442928230863465674813919123162824586"
	numberString += "17866458359124566529476545682848912883142607690042"
	numberString += "24219022671055626321111109370544217506941658960408"
	numberString += "07198403850962455444362981230987879927244284909188"
	numberString += "84580156166097919133875499200524063689912560717606"
	numberString += "05886116467109405077541002256983155200055935729725"
	numberString += "71636269561882670428252483600823257530420752963450"

	# Make a list of all the suspected indices which might 
	# be the start of the sequence with the largest product
	indices = range(0, len(numberString))

	# Identify each index where the index itself, or one of the following
	# 12 characters, are '0' and remove them
	for i in indices:
		if '0' in numberString[i:i + 13]:
			indices[i] = -1

	newIndices = [n for n in indices if n != -1]
	indices = newIndices
	del(newIndices)

	# Now to find the largest product
	result = 0
	
	for index in indices:
		sequenceString = numberString[index:index + 13]
		sequence = list(map(lambda x: int(x), sequenceString))
		prod = reduce((lambda x, y: x * y), sequence)

		if prod > result:
			result = prod

	print result
	return result


FindLargestProductInASeries()
# Returns 23514624000





