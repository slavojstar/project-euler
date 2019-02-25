# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

from Utilities import IsPalindrome, ConvertToBase

def FindDoubleBasePalindromes():
	palSum = 0

	for i in range(1000000):
		if not IsPalindrome(i) or not IsPalindrome(int(ConvertToBase(i, 2))):
			continue
		else:
			palSum += i

	print(palSum)
	return palSum

def BetterFindDoubleBasePalindromes():
	# The number 'xyz' can be used to generate the palindromes
	# 'xyzyx' and 'xyzzyx', so therefore, in base b, every
	# number under b^n can generate two palindromes under
	# b^2n.
	palSum = 25 # 1, 3, 5, 7, 9 are palindromes base 2 so add them on

	for i in range(1, 1000):
		stringPal = str(i)

		# pal1 is 'xyzzyx'
		pal1 = int(stringPal + stringPal[::-1])
		if IsPalindrome(ConvertToBase(pal1, 2)):
			palSum += pal1
		# pal2 is 'xyzyx'
		if not len(stringPal) == 1:
			pal2 = int(stringPal + stringPal[len(stringPal) - 2::-1])
			if IsPalindrome(ConvertToBase(pal2, 2)):
				palSum += pal2

	print(palSum)
	return palSum

BetterFindDoubleBasePalindromes()
# Returns 872187
