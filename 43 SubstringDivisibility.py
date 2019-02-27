'''Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.'''

import Utilities

def FindSubstringDivisibility():

	pans = Utilities.Permute('0123456789')
	panSum = 0

	for pan in pans:
		if not int(pan[1:4]) % 2 == 0:
			continue
		elif not int(pan[2:5]) % 3 == 0:
			continue
		elif not int(pan[3:6]) % 5 == 0:
			continue
		elif not int(pan[4:7]) % 7 == 0:
			continue
		elif not int(pan[5:8]) % 11 == 0:
			continue
		elif not int(pan[6:9]) % 13 == 0:
			continue
		elif not int(pan[7:]) % 17 == 0:
			continue
		else:
			panSum += int(pan)

	print(panSum)
	return panSum

FindSubstringDivisibility()
# Returns 16695334890