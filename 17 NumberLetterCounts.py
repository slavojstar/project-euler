# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used? 

def FindNumberLetterCounts():

	letterCount = 0

	# 1 - 9
	# There isn't a pattern to the first 9 no.s
	# so we just add their letter counts
	letterCount =+ 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 # = 36

	# 10 - 19
	# Again, not really a pattern:
	letterCount += 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 # = 70

	# 20 - 99
	# For each 10 no.s we have the 10s prefix 10 times then
	# the 1 - 9 sequence which we know has 36 letters
	letterCount += 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * 36 # = 748

	# So 1 - 99 has 36 + 70 + 748 = 854 letters

	# 100 - 999
	# Numbers like "Four hundred and seventy eight". So we always have the 100s
	# prefix, the "hundred and", and then the 10s and then the units.
	# Whole hundreds are a special case ("two hundred")

	# We have 1 - 9 occurring 100 times:
	letterCount += 36 * 100 # = 3600

	# 1 - 99 occurring 9 times:
	letterCount += 9 * 854 # = 7686

	# "hundred" occurring 9 times:
	letterCount += 9 * 7 # = 63

	# "hundred and" occurring 9 * 99 times:
	letterCount += 9 * 99 * 10 # = 8910

	# We also have "one thousand"
	letterCount += 11

	print(letterCount)
	return letterCount

FindNumberLetterCounts()
# Returns 21124