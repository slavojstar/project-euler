# Find the number after 40755 that is triangular, pentagonal, and hexagonal

import math

def FindTriangularPentagonalandHexagonal():
	# All Hexagonal numbers are triangular, so we're just
	# looking for a hexagonal number which is also pentagonal.

	# Start from the 144th hexagonal number
	i = 144

	while True:
		hexa = i * (2 * i - 1)
		penta = math.sqrt(1 + 24 * hexa)
		if penta % 6 == 5 and penta == math.floor(penta):
			break
		else:
			i += 1

	print(hexa)
	return hexa

FindTriangularPentagonalandHexagonal()
# Returns 1533776805


