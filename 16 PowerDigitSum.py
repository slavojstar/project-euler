# What is the sum of the digits of the number 2^1000?

import math

def FindPowerDigitSum():
	# Every +ve number n has Ceiling(log_10(n)) digits
	# Using this, let's calculate how many digits
	# 2^1000 has:

	n = math.pow(2, 1000)

	digits = int(math.ceil(math.log(n, 10)))

	print digits
	# Output: 302.0

	# So 2^1000 = 0.k * 10 ^ 302, where k has 302 digits.
	# Rearranging gives us that 0.k = 10^(1000 * log_10(2) - 302).
	# Lets calculate this:
	startN = math.pow(10, 1000 * math.log(2, 10) - 302)
	print startN
	# Output: 0.107150860719
	# So we know that n^1000 starts with 1071...

	# Notice that powers of 2 cycle with period 4
	# and 2^4n for all natural n ends in 6

FindPowerDigitSum()
#Returns