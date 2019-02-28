# Find the number after 40755 that is triangular, pentagonal, and hexagonal

import math

def FindTriangularPentagonalandHexagonal():

	i = 40756

	while True:
		endI = i % 10

		if not endI == 1 or not endI == 0 or not endI == 5 or not endI == 6:
			i += 1
			continue

		tH = math.sqrt(1 + 8 * i)
		p = math.sqrt(1 + 24 * i)
		if (tH == math.floor(tH) and tH % 4 == 3 and\
			p == math.floor(p) and p % 6 == 5):
			break
		else:
			i += 1
			continue

	print(i)
	return i

FindTriangularPentagonalandHexagonal()
# Returns ????


	