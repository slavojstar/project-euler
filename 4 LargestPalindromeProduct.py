# Find the largest palindrome made from the product of two 3-digit numbers.

import sys
from Utilities import IsPalindrome

def FindLargestPalindromeProduct():
	palindrome = 0

	for i in range(999, 99, -1):
		for j in range(999, i - 1, -1):
			if IsPalindrome(i * j) and i * j > palindrome:
				palindrome = i * j

	print palindrome
	return palindrome

FindLargestPalindromeProduct()
# Returns 906609