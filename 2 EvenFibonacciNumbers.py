# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def FindFib(i):
	if i > 2:
		return FindFib(i - 1) + FindFib(i - 2)
	else:
		return 1

def FindEvenFibonacciNumbers():
	sum = 0
	i = 1

	while True:
		if FindFib(i) > 4000000:
			break
		if FindFib(i) % 2 == 0:
			sum += FindFib(i)
		i += 1

	print sum

FindEvenFibonacciNumbers()
# Returns 4613732