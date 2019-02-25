# coding=utf-8

# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

def FindLargestProductInAGrid():
	# Create a 20x20 multi-dimensional list to house
	# the grid from the problem
	grid = [[0 for x in range(20)] for y in range(20)]

	# Create a grid of indices
	# indices = [[[0, 0] for x in range(20)] for y in range(20)]
	
	# Read the grid into the list, and insert the indices
	with open("11 GridProduct.txt") as GridFile:
		i = 0
		for line in GridFile:
			# End of line character needs snipping off
			line = line[:-1]

			lineList = line.split(' ')
			for j in range(20):
				grid[i][j] = int(lineList[j])
				# indices[i][j] = [i, j]
			i += 1

	# There was no end of line character in the final row,
	# so we accidently snipped of the second digit of the
	# last number. Fixing this:
	grid[19][19] = 48

	result = 0

	# Check the horizontal groups of four
	for i in range(20):
		for j in range(17):
			subGridHor = grid[i][j: j + 4]
			prod = reduce((lambda x, y: x * y), subGridHor)
			if prod > result:
				result = prod
				print "Horizontal:"
				print str(i) + ", " + str(j)
				print result

	# Check the vertical groups of four
	for i in range(17):
		for j in range(20):
			subGridVer = []
			for k in range(4):
				subGridVer.append(grid[i + k][j])
			prod = reduce((lambda x, y: x * y), subGridVer)
			if prod > result:
				result = prod
				print "Vertical:"
				print str(i) + ", " + str(j)
				print result

	# Check the diagonal groups of four
	# (direction is top left to bottom right)
	for i in range(17):
		for j in range(17):
			subGrid1Dia = []
			for k in range(4):
				subGrid1Dia.append(grid[i + k][j + k])
			prod = reduce((lambda x, y: x * y), subGrid1Dia)
			if prod > result:
				result = prod
				print "1st Diagonal:"
				print str(i) + ", " + str(j)
				print result

	# Check the diagonal groups of four
	# (direction is top right to bottom left)
	for i in range(3, 20):
		for j in range(17):
			subGrid2Dia = []
			for k in range(4):
				subGrid2Dia.append(grid[i - k][j + k])
			prod = reduce((lambda x, y: x * y), subGrid2Dia)
			if prod > result:
				result = prod
				print "2nd Diagonal:"
				print str(i) + ", " + str(j)
				print result

	print result

FindLargestProductInAGrid()
# Returns 70600674