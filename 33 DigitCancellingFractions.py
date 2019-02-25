''' 
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def FindDigitCancellingFractions():

	fracs = []
	literalFracs = []
	for num in range(10, 100):
		# We need denom > num, hence the following range
		for denom in range(num + 1, 100):

			# 'We shall consider fractions like, 30/50 = 3/5, to be trivial examples.''
			if num % 10 == 0 and denom % 10 == 0:
				continue

			strNum = str(num)
			strDenom = str(denom)

			# Check whether denom and num share a digit in common
			if not (strNum[0] in strDenom) and not (strNum[1] in strDenom):
				continue

			elif strNum[0] in strDenom:
				newNum = int(strNum[1])

				listDenom = list(strDenom)
				listDenom.remove(strNum[0])

				newDenom = int(listDenom[0])

				if num * newDenom == newNum * denom:
					literalFracs.append(strNum + " / " + strDenom)

			elif strNum[1] in strDenom:
				newNum = int(strNum[0])

				listDenom = list(strDenom)
				listDenom.remove(strNum[1])

				newDenom = int(listDenom[0])

				if num * newDenom == newNum * denom:
					literalFracs.append(strNum + " / " + strDenom)
					fracs.append(str(newNum)  + " / " + str(newDenom))

	print(literalFracs)
	print(fracs)

FindDigitCancellingFractions()
# Answer is 100









