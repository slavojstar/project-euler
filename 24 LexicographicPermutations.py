# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from Utilities import FindLex

def FindLexicographicPermutations():

	# In the ordered list (size n!) of lexicographic permutations of n
	# distinct digits, the first n! / n = (n - 1)! permutations will be of the form
	# 'n_0[lexicographic perms of the remaining digits]' where n_0 is the
	# smallest digit. The second (n - 1)! perm.s will be of the same form
	# but with n_1 instead of n_0 etc.

	# Here n = 10, so there are 10! = 3628800 perms split into 10 sections
	# of size 9! = 362880. 10^6 / 362880 = 2.755731922398589, so the 10^6th
	# permutation will be in the 2nd block (starts from the 0th block), and
	# so will start with a 2. We can iterate this.

	# I've written the generic form in Utilities.
	print(FindLex(999999, range(10)))
	return FindLex(999999, range(10))

FindLexicographicPermutations()
# Returns 2783915460
