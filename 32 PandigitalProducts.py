# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

def FindPandigitalProducts():
	# Lets call the product x * y = z. Then x and y
	# cannot both be 3 digit numbers because then z
	# would be a 5 digit number, so we would necessarily
	# have at least 1 repeated number.

	# x cannot be equal to y, so in every product we need
	# either x < y or y < x. WLOG we can assume that x < y.

	# Clearly x and y cannot both be 1 digit numbers, and (a 
	# little less clearly), they can't both be 2 digit numbers.

	# So we need that x is a 2 digit number and that y is a 
	# 3 digit number (or maybe that x is a 1 digit number
	# and that y is a 4 digit number). It's also the case that if we have a 1
	# in the digit column of either number, we are guaranteed
	# a repetition, so that can't be the case.

	# Also, for the product to be pandigital in 1 through 9
	# we can't have any zeros anywhere

	zeds = []
	strZeds = []

	# Check the instances where x has 1 digit and y has 4
	for x in range(1, 10):
		strX = str(x)

		if '0' in strX:
			continue

		if strX[-1] == '1':
			continue

		for y in range(1234, 9877):
			strY = str(y)

			if '0' in strY:
				continue

			if strY[-1] == '1':
				continue

			if strX[0] in strY:
				continue

			# Check if there are any duplicates within y
			if len(set(strY)) < 4:
				continue

			z = int(x * y)
			strZ = str(z)
			concat = strX + strY

			if '0' in strZ:
				continue

			if len(strZ) != 4:
				continue

			# Check if there are any duplicates within z
			if len(set(strZ)) < 4:
				continue

			if (concat[0] in strZ or concat[1] in strZ or concat[2] in strZ or
				concat[3] in strZ or concat[4] in strZ):
				continue
			elif z in zeds:
				continue
			else:
				strZeds.append(strX + " x " + strY + " = " + strZ)
				zeds.append(z)


	# Check the instances where x has 2 digits and y has 3
	for x in range(12, 99):
		strX = str(x)

		if '0' in strX:
			continue

		if strX[-1] == '1':
			continue

		#Check if there are any duplicates within x
		if len(set(strX)) < 2:
			continue

		for y in range(123, 988):
			strY = str(y)

			if '0' in strY:
				continue

			if strY[-1] == '1':
				continue

			if strX[0] in strY or strX[1] in strY:
				continue

			# Check if there are any duplicates within y
			if len(set(strY)) < 3:
				continue

			z = int(x * y)
			strZ = str(z)
			concat = strX + strY

			if '0' in strZ:
				continue

			if len(strZ) != 4:
				continue

			# Check if there are any duplicates within z
			if len(set(strZ)) < 4:
				continue

			if (concat[0] in strZ or concat[1] in strZ or concat[2] in strZ or
				concat[3] in strZ or concat[4] in strZ):
				continue
			elif z in zeds:
				continue
			else:
				strZeds.append(strX + " x " + strY + " = " + strZ)
				zeds.append(z)

	print(strZeds)
	print(zeds)
	print(sum(zeds))
	return sum(zeds)

FindPandigitalProducts()

# Returns 45228










