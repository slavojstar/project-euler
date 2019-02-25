#Find the maximum path sum from top to bottom of the triangle below:
'''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

def FindMaximumPathSum():
	# Construct the triangle
	triangle = []

	for i in range(15):
		triangle.append([0] * (i + 1))
	
	with open("18 Triangle.txt") as triangleFile:
		i = 0
		for line in triangleFile:
			# End of line character needs snipping off:
			if not i == 14:
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

FindMaximumPathSum()
# Returns 1074