# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def FindCountingSundays():

	# The 1st of Jan 1901 was a tuesday:
	week = [1, 2, 3, 4, 5, 6, 0]

	september = april = june = november =  list(range(30))
	january = march = may = july = august = october = december = list(range(31))
	february = list(range(28))
	februaryLeap = list(range(29))

	year = january + february + march + april + may + june + july +\
		august + september + october + november + december

	leapYear = january + februaryLeap + march + april + may + june + july +\
		august + september + october + november + december

	currentYear = 1901
	day = 0
	yearDay = 0
	sunSum = 0

	while currentYear < 2001:
		if currentYear % 4 == 0:
			for i in leapYear:
				if week[day % 7] == 6 and leapYear[yearDay] == 0:
					sunSum += 1
				day += 1
				yearDay += 1
		else:
			for i in year:
				if week[day % 7] == 6 and year[yearDay] == 0:
					sunSum += 1
				day += 1
				yearDay += 1
		yearDay = 0
		currentYear += 1

	print(sunSum)
	return sunSum

FindCountingSundays()

# Returns 171