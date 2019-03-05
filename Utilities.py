import math
import random
import pdb
import time
from itertools import chain, combinations
import numbers
import json
from collections.abc import Iterable
import ast

def ConvertToBase(n, b):
	''' Converts n to n (base b). Returns an integer.'''
	if b > 10:
		print("Error: base b should be less than or equal to 10")
		return n

	if b == 0:
		print("Error: base b cannot be 0")
		return n

	if not isinstance(n, int):
		print("ConvertToBase({0}, {1}): Warning: {0} is not an integer".format(n, b))
		return n

	if not isinstance(b, int):
		print("ConvertToBase({0}, {1}): Warning: {1} is not an integer".format(n, b))
		return n

	if n == 0:
		return 0

	if b == 1:
		return "1" * n

	sgn = n / math.fabs(n)

	if sgn == -1:
		n = int(math.fabs(n))

	result = ""
	remainder = 0

	while n > 0:
		remainder = n % b
		n = int(n / b)
		result = str(remainder) + result

	if sgn == -1:
		result = "-" + result
		return int(result)
	else:
		return int(result)



def GCDEuclid(a, b):
	''' Returns the GCD of integers a and b using Euclid's algorithm. '''

	if not isinstance(a, int):
		print("GCDEuclid({0}, {1}): Warning: {0} is not an integer".format(a, b))
		return 1

	if not isinstance(a, int):
		print("GCDEuclid({0}, {1}): Warning: {1} is not an integer".format(a, b))
		return 1

	while b != 0:
		t = b
		b = a % b
		a = t

	return a

def PowerModulo(m, n, p):
	''' Returns m ^ n modulo p '''

	if not isinstance(m, int):
		print("PowerModulo({0}, {1}, {2}): Warning: {0} is not an integer".format(m, n, p))
	if not isinstance(n, int):
		print("PowerModulo({0}, {1}, {2}): Warning: {1} is not an integer".format(m, n, p))
	if not isinstance(p, int):
		print("PowerModulo({0}, {1}, {2}): Warning: {2} is not an integer".format(m, n, p))
		return


	nBin = str(ConvertToBase(n, 2))

	checkMod = m

	for i in range(1, len(nBin)):
		if nBin[i] == '0':
			checkMod = int(math.pow(checkMod, 2)) % p
		else:
			checkMod = int(math.pow(checkMod, 2) * m) % p

	return checkMod

def MillerRabin(p, k):
	''' Returns false => p is not prime
	Returns true => p is prime with probability 1 - (3/4) ^ k '''

	if not isinstance(p, int):
		print("MillerRabin({0}, {1}): Warning: {0} is not an integer".format(p, k))
		return
	if not isinstance(k, int):
		print("MillerRabin({0}, {1}): Warning: {1} is not an integer".format(p, k))
		return

	# First we get p in the form (2 ^ twoCounter) * evenHelper + 1
	evenHelper = p - 1
	twoCounter = 0

	while True:
		evenHelper /= 2
		twoCounter += 1
		if (evenHelper % 2 == 1):
			break

	# Create a k length array of random integers less than p
	# which don't divide p.
	randArray = [0] * k

	# The position in randArray in which to insert the random integer
	position = 0

	while randArray[k - 1] == 0:
		numToInsert = random.randint(2, p - 1)
		if p % numToInsert == 0 or numToInsert in randArray:
			continue
		else:
			randArray[position] = numToInsert
			position += 1

	testCondition = True
	position = 0

	while testCondition:
		if position == len(randArray):
			break

		b = PowerModulo(randArray[position], evenHelper, p)

		for i in range(twoCounter + 1):
			if i == twoCounter:
				testCondition = False
				break
			elif b == 1 or b == p - 1:
				position += 1
				break
			else:
				b = int(math.pow(b, 2)) % p

	return testCondition

def IsPalindrome(a):
	''' Returns True if a is a palindrome, False if not. '''

	if not isinstance(a, (int, float, str)):
		print("IsPalindrome({0}): Warning: {0} is not an int, float or str.".format(a))

	if a < 0:
		a *= -1

	s = str(a)

	for i in range(0, len(s)):
		if s[i] == s[len(s) - i - 1]:
			continue
		else:
			return False

	return True

def PollardRhoAlgo(n):
	''' Returns a factor of n using Pollard's Rho Algorithm '''

	if not isinstance(n, int):
		print("PollardRhoAlgo({0}): Warning: {0} is not an int.".format(n))

	xFixed = 2
	cycleSize = 2
	x = 2
	factor = 1

	while factor == 1:
		count = 1
		while count <= cycleSize and factor <= 1:
			x = (x * x + 1) % n
			factor = GCDEuclid(x - xFixed, n)
			count += 1
		cycleSize *= 2
		xFixed = x

	return factor

def FindLex(k, elements):
	''' Returns the kth lexicographic permutation of the elements
	array as a string'''

	if not isinstance(k, int):
		print("FindLex({0}, {1}): Warning: {0} is not an int.".format(k, elements))
		return str(elements)

	if not isinstance(elements, (str, list, set)):
		print("FindLex({0}, {1}): Warning: {1} is not a str, list, or set.".format(k, elements))
		return

	if len(elements) == 1:
		return str(elements[0])
	else:
		elements = list(elements)
		elements.sort()

		sectionLength = math.factorial(len(elements) - 1)
		d = int(math.floor(k / sectionLength))
		k = k % sectionLength
		element = elements[d]
		elements.remove(element)

		return str(element) + FindLex(k, elements)

def IsPrime(n):
	''' Returns true if n is prime, false otherwise (use MillerRabin()
	for large n) '''
	if not isinstance(n, int):
		print("IsPrime({0}): Warning: {0} is not an int.".format(n))
		return

	if n <= 0:
		return False
	if n == 1:
		return False
	elif n < 4:
		return True
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	else:
		r = int(math.floor(math.sqrt(n)))
		f = 5
		while f <= r:
			if n % f == 0:
				return False
			if n % (f + 2) == 0:
				return False
			f += 6
		return True

def NPrimes(n):
	''' Returns an array of the first n primes (not very efficient) '''

	if not isinstance(n, int):
		print("NPrimes({0}): Warning: {0} is not an int.".format(n))

	primes = []
	i = 1

	while len(primes) != n:
		if IsPrime(i):
			primes.append(i)
		i += 1
	return primes

def LimPrimes(loLimit, hilimit):
	''' Returns an array of all the primes from loLimit and
	up to but not including the hilimit (not very efficient) '''
	if not isinstance(loLimit, (int, float)):
		print("LimPrimes({0}, {1}): Warning: {0} is not an int or a float.".format(loLimit, hiLimit))
		return

	if not isinstance(hiLimit, (int, float)):
		print("LimPrimes({0}, {1}): Warning: {1} is not an int or a float.".format(loLimit, hiLimit))
		return

	if loLimit >= hiLimit:
		print("LimPrimes({0}, {1}): Warning: The lower limit cannot be \
			higher or equal to than the higher limit.".format(loLimit, hiLimit))
		return

	if loLimit < 0:
		return LimPrimes(0, hiLimit)

	primes = []
	i = loLimit

	while i < hiLimit:
		if IsPrime(i):
			primes.append(i)
		i += 1
	return primes
	


def PrimeSumUnderK(n, k, primes = []):
	''' Returns the amount of ways you can sum primes under k
	, or the primes from a given list primes, to get n '''

	if not isinstance(n, int):
		print("PrimeSumUnderK({0}, {1}, {2}): Warning: {0} is not an int.".format(n, k, primes))
		return

	if not isinstance(k, (int, float)):
		print("PrimeSumUnderK({0}, {1}, {2}): Warning: {1} is not an int or a float.".format(n, k, primes))
		return

	if not isinstance(primes, list):
		print("PrimeSumUnderK({0}, {1}, {2}): Warning: {2} is not a list".format(n, k, primes))
		return

	if n < k:
		k = n

	if k < 2 or n < 2:
		raise Exception("No primes exist below 2.")

	if k == 2 and n == 2:
		return 1

	if not primes:
		primes = LimPrimes(0, k + 1)
	else:
		# If any of the primes in the array are above k, we
		# discard them
		primes = [x for x in primes if x <= k]
		primes.sort()
	
	primes = primes[::-1]

	ways = 0

	for prime in primes:
		diff = n - prime
		if diff == 0:
			ways += 1
			continue
		try:
			newWays = PrimeSumUnderK(diff, prime, primes)
		except:
			continue
		ways += newWays

	return ways

def NumberSums(n, k, summands = []):
	''' Returns the amount of ways you can sum the summands
	to get n. If summands is empty and k = n NumberSums returns p(n)
	where p is the partition function '''

	if not isinstance(n, int):
		print("NumberSums({0}, {1}, {2}): Warning: {0} is not an int.".format(n, k, summands))
		return

	if not isinstance(k, (int, float)):
		print("NumberSums({0}, {1}, {2}): Warning: {1} is not an int or a float.".format(n, k, summands))
		return

	if not isinstance(summands, list):
		print("NumberSums({0}, {1}, {2}): Warning: {2} is not a list".format(n, k, summands))
		return

	if n == 1 or n == 0:
		return 1

	if n < k:
		k = n

	if not summands:
		summands = range(1, k + 1)
	else:
		# If there exist any summands greater than n, we
		# discard them
		summands = [x for x in summands if x <= k]
		summands.sort()

	summands = summands[::-1]

	ways = 0

	for summand in summands:
		diff = n - summand
		newWays = NumberSums(diff, summand, summands)
		ways += newWays

	return ways

def NumberSumsII(n, m, summands = [], numDict = {}):
	''' Returns the amount of ways you can sum the summands
	to get n. If summands is empty and m = n NumberSums returns p(n)
	where p is the partition function. '''

	if not isinstance(n, int):
			print("NumberSumsII({0}, {1}, {2}, {3}): Warning: {0} is not an int.".format(n, m, summands, numDict))
			return

	if not isinstance(m, (int, float)):
		print("NumberSumsII({0}, {1}, {2}, {3}): Warning: {1} is not an int or a float.".format(n, m, summands, numDict))
		return

	if not isinstance(summands, list):
		print("NumberSumsII({0}, {1}, {2}, {3}): Warning: {2} is not a list".format(n, m, summands, numDict))
		return

	if not isinstance(numDict, dict):
		print("NumberSumsII({0}, {1}, {2}, {3}): Warning: {2} is not a dict".format(n, m, summands, numDict))
		return	

	if n == 1 or n == 0:
		return 1

	if n < m:
		m = n

	if not summands:
		summands = list(range(1, m + 1))
	else:
		# If there exist any summands greater than n, we
		# discard them
		summands = [x for x in summands if x <= m]
		summands.sort()

	summands = summands[::-1]

	newDict = {k: v for k, v in numDict.items() if k[0] <= m}

	ways = 0

	for summand in summands:
		diff = n - summand
		if (diff, summand) in newDict:
			newWays = newDict[(diff, summand)]
		else:
			newWays = NumberSumsII(diff, summand, summands, numDict)
			numDict.update({(diff, summand): newWays})
			print(numDict)
		ways += newWays

	return ways

# Doesn't work
def EulerPartition(n):
	''' Returns p(n) using Euler's recurrence relation '''
	if n <= 0:
		print("EulerPartition({0}): Warning: Partition cannot be made of a non-negative integer.".format(n))

	if not isinstance(n, (int, float)):
		print("EulerPartition({0}): Warning: {0} is not an int or a float".format(n))

	if n == 1:
		return 1

	coeffs = []
	for i in range(1, n + 1):
		r = i * (3 * i - 1) / 2
		if r >= n:
			break
		elif r % 2 != 0:
			coeffs.append(-r)
		else:
			coeffs.append(r)

		k = i * (3 * i + 1) / 2
		if k >= n:
			break
		elif k % 2 != 0:
			coeffs.append(-k)
		else:
			coeffs.append(k)

	partition = 0
	for i in coeffs:
		if i < 0:
			partition += EulerPartition(int(-i))
		else:
			partition -= EulerPartition(int(i))

	return partition

def PowerSet(iterable):
	''' Returns the power set of iterable '''
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def PrimeFactors(n):
	''' Returns a list of the prime factors of an integer n '''

	if n <= 0:
		print("PrimeFactors({0}): Warning: PrimeFactors cannot be found of a non-negative integer.".format(n))
		return

	if not isinstance(n, (int, float)):
		print("PrimeFactors({0}): Warning: {0} is not an int or a float".format(n))	
		return

	if IsPrime(n):
		return [n]

	potentialPrimes = LimPrimes(0, math.sqrt(n) + 1)
	factors = []
	i = 0

	while n > 1:
		prime = potentialPrimes[i]
		if n % prime == 0:
			factors.append(prime)
			n = int(n / prime)
			if IsPrime(n):
				factors.append(n)
				break
		else:
			i += 1

	return factors

def NumberOfFactorsOf(n):
	''' Returns the number of factors of a positive integer n. '''
	if n == 1:
		return 1

	if n < 1:
		print("NumberOfFactorsOf({0}): Warning: Argument cannot be less than 1".format(n))
		return


	if not isinstance(n, int):
		print("NumberOfFactorsOf({0}): Warning: {0} is not an int.".format(n))
		return

	primeFactors = PrimeFactors(n)

	return len(set(PowerSet(primeFactors)))

def FactorsOf(n):
	''' Returns a list of the factors of n '''
	if n == 1:
		return [1]

	if n == 0:
		print("FactorsOf(0): Warning: Zero has infinite factors.")
		return 

	if not isinstance(n, int):
		print("FactorsOf({0}): Warning: {0} is not an int.".format(n))
		return

	factors = []

	if n < 0:
		factors.append(-1)
		n *= -1

	factorDecomp = set(PowerSet(PrimeFactors(n)))

	for tup in factorDecomp:
		prod = 1
		if not tup:
			factors.append(1)
			continue
		else:
			for i in tup:
				prod *= i
		factors.append(prod)

	return factors

def ProperFactorsOf(n):
	''' Returns a list of the proper factors of n. '''
	nFac = FactorsOf(n)
	nFac.remove(n)
	return nFac

def IsAmicable(n):
	''' Returns (False, 0) if n is not an amicable number and
	(True, k) if n is amicable with k. '''
	nFacSum = sum(ProperFactorsOf(n))

	# Return false if n is a perfect number
	if nFacSum == n:
		return (False, 0)
	
	kFacSum = sum(ProperFactorsOf(nFacSum))
	if kFacSum == n:
		return (True, nFacSum)
	else:
		return(False, 0)

def updateJsonfile(fileName, pythonDict):
	''' Updates a single json object in a file with the python dict
	object '''
	if not isinstance(fileName, str):
		print("updateJsonfile({0}, {1}): Warning: {0} is not a str.".format(fileName, pythonDict))
		return

	if not isinstance(pythonDict, dict):
		print("updateJsonfile({0}, {1}): Warning: {1} is not a dict.".format(fileName, pythonDict))
		return

	jsonFileRead = open(fileName, 'r')
	data = json.load(jsonFileRead)
	jsonFileRead.close()

	data.update(pythonDict)
	jsonObject = json.dumps(data)

	jsonFileWrite = open(fileName, 'w+')
	jsonFileWrite.write(jsonObject)
	jsonFileWrite.close()

def IsPandigital(s, n):
	''' Returns True is s is pandigital in 1 to n '''
	pans = list(range(1, n + 1))
	esses = str(s)
	esses = list(map(lambda x: int(x), esses))

	if not isinstance(s, int):
		print("IsPandigital({0}, {1}): Warning: {0} is not an int.".format(s, n))
		return

	if not isinstance(n, int):
		print("IsPandigital({0}, {1}): Warning: {1} is not an int.".format(s, n))
		return

	if n < 1 or n > 9:
		print("IsPandigital({0}, {1}): Warning: n ({1}) must cannot be less than 1 or greater than 9.".format(s, n))
		return

	for pan in pans:
		if pan in esses:
			esses.remove(pan)
		else:
			return False

	if not esses:
		return True
	else:
		return False

def Partition(n):
	''' Returns the partition number of n '''
	if not isinstance(n, int):
		print("Partition({0}): Warning: {0} is not an int.".format(n))

	jsonFileRead = open('PartitionObject.json', 'r')
	dataDict = json.load(jsonFileRead)
	jsonFileRead.close()

	newDataDict = {}
	for k in dataDict:
		newK = ast.literal_eval(k)
		newDataDict.update({newK: dataDict[k]})

	if (n, n) in newDataDict:
		return newDataDict[(n, n)]

	parTuple = PartitionHelper(n, n, newDataDict)
	p = parTuple[0]
	newDict = parTuple[1]
	newDict.update({(n, n): p})

	finalDict = {}
	for k in newDict:
		newK = str(k)
		finalDict.update({newK: newDict[k]})

	jsonObject = json.dumps(finalDict)

	jsonFileWrite = open('PartitionObject.json', 'w+')
	jsonFileWrite.write(jsonObject)
	jsonFileWrite.close()

	return p

def PartitionHelper(n, m, numDict = {}):

	if not isinstance(numDict, dict):
		print("NumberSumsII({0}, {1}, {2}): Warning: {2} is not a dict".format(n, m, numDict))
		return	

	if n == 1 or n == 0:
		return (1, numDict)

	if n < m:
		m = n
	
	summands = list(range(1, m + 1))

	summands = summands[::-1]

	newDict = {k: v for k, v in numDict.items() if k[0] <= m}

	ways = 0

	for summand in summands:
		diff = n - summand
		if (diff, summand) in newDict:
			newWays = newDict[(diff, summand)]
		else:
			newWays = PartitionHelper(diff, summand, numDict)[0]
			if summand > diff:
				summand = diff
			numDict.update({(diff, summand): newWays})
		ways += newWays

	return (ways, numDict)

def IsPandigital(s, n):
	''' Takes a string of integers and returns True if it is
	pandigital from 1 to n and False otherwise '''

	if not isinstance(s, str):
		print("IsPandigital({0}, {1}): Warning: {0} is not a string.".format(s, n))
		return
	if not isinstance(n, int) or n < 1 or n > 9:
		print("IsPandigital({0}, {1}): Warning: {1} must be an int between 1 and 9 (incl.)".format(s, n))
		return

	# Check if there are any duplicates:
	setS = set(s)
	if len(setS) > len(s):
		return False

	for i in range(1, n + 1):
		if str(i) in setS:
			setS.remove(str(i))
		else:
			return False

	if setS:
		return False
	else:
		return True

def NthChampernowne(n):
	''' Returns the nth digit in the fractional part of Champernowne's
	constant '''

	if not isinstance(n, int) or n < 1:
		print("NthChampernowne({0}): Warning: {0} must be an integer greater than 0.".format(n))

	# There are exactly 9 * n * (10 ** (n - 1)) numbers that have n digits. So you can
	# partition the fractional part of Champernowne's constant into bins of size
	# 9 * n * (10 ** (n - 1)). We want to find in which bin is the nth digit, and therefore
	# how many digits has the number it is part of. (i.e. 12th Champernown is the 1st '1'
	# of '11' in the decimal expansion, so it is in the 2nd bin, and therefore is part of 
	# a number with 2 digits).

	digits = 1
	lowerBoundary = 0
	upperBoundary = 0

	while True:
		upperBoundary = lowerBoundary + 9 * digits * (10 ** (digits - 1))
		if n > lowerBoundary and n <= upperBoundary:
			break
		else:
			digits += 1
			lowerBoundary = upperBoundary

	# The interval is how far into its bin the digit is
	interval = n - lowerBoundary - 1
	# firstNum is the first number in the bin
	firstNum = 10 ** (digits - 1)
	# num is the nth number into the bin
	num = math.floor(interval / digits)
	# microNum is which character in the number the nth digit is
	microNum = (interval % digits)
	numToExtract = str(firstNum + num)

	return int(numToExtract[microNum])

def Permute(s):
	''' Returns a list of permutations of a string s '''
	if not isinstance(s, str):
		print("Permute({0}): Warning: {0} must be a string.".format(s))
	if len(s) == 1:
		return [s[0]]
	elif len(s) == 2:
		return [s[0] + s[1], s[1] + s[0]]
	else:
		perms = []
		listS = list(s)
		for elem in listS:
			newListS = listS.copy()
			newListS.remove(elem)
			newStringS = ''
			for newElem in newListS:
				newStringS += newElem
			for perm in Permute(newStringS):
				perms.append(elem + perm)

	return perms

def LastDigs(n, p, s):
	''' Returns the last s digits of n ^ p where n and p
	are natural numbers greater than 0 '''
	if not isinstance(n, int) or n < 1:
		print("LastDigs({0}, {1}, {2}): Warning: {0} must be an integer greater than 0.".format(n, p, s))

	if not isinstance(p, int) or p < 1:
		print("LastDigs({0}, {1}, {2}): Warning: {1} must be an integer greater than 0.".format(n, p, s))

	if not isinstance(s, int)or s < 1:
		print("LastDigs({0}, {1}, {2}): Warning: {2} must be an integer greater than 0.".format(n, p, s))

	strN = str(n)

	if len(strN) > s:
		n = int(strN[len(strN) - s:])

	res = n

	for i in range(p - 1):
		strRes = str(res)
		if len(strRes) > s:
			res = int(strRes[len(strRes) - s:])
		res *= n

	finalStr = str(res)
	finalInt = int(finalStr[len(finalStr) - s:])
	
	return finalInt
































