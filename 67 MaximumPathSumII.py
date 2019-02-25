# Find the maximum total from top to bottom in "67 Triangle.txt",
# a 15K text file containing a triangle with one-hundred rows.

def FindMaximumPathSumII():
	# Construct the triangle
	triangle = []

	for i in range(100):
		triangle.append([0] * (i + 1))
	
	with open("67 Triangle.txt") as triangleFile:
		i = 0
		for line in triangleFile:
			# End of line character needs snipping off:
			if not i == 99:
				line = line[:-1]
			lineList = line.split(' ')
			for j in range(i + 1):
				triangle[i][j] = int(lineList[j])
			i += 1

	for i in range(len(triangle) - 1, 0, -1):
		for j in range(len(triangle[i]) - 1):
			triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])

	print triangle[0][0]
	return triangle[0][0]

FindMaximumPathSumII()
# Returns 7273