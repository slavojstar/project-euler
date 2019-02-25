# Find the number of triangles for which the interior contains the origin

import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

def FindTriangleContainment():

	# List containing lists of length 6 representative of each
	# triangle
	triangles = []

	with open("102 Triangles.txt") as TriFile:
		for line in TriFile:
			# Chop of the end-of-line character
			line = line[:-1]
			triList = line.split(',')
			for i in range(6):
				triList[i] = int(triList[i])
			triangles.append(triList)
	
		
	for triangle in triangles:
		# the composition of each triangle list is as follows
		# [x_0, y_0, x_1, y_1, x_2, y_2]
		x_0 = triangle[0]
		y_0 = triangle[1]
		x_1 = triangle[2]
		y_1 = triangle[3]
		x_2 = triangle[4]
		y_2 = triangle[5]

		# Remove those triangles which lie entirely either side of
		# x = 0 or y = 0.
		if x_0 > 0 and x_1 > 0 and x_2 > 0:
			triangles.remove(triangle)
			continue
		elif x_0 < 0 and x_1 < 0 and x_2 < 0:
			triangles.remove(triangle)
			continue
		elif y_0 > 0 and y_1 > 0 and y_2 > 0:
			triangles.remove(triangle)
			continue
		elif y_0 < 0 and y_1 < 0 and y_2 < 0:
			triangles.remove(triangle)
			continue

		# Calculating the gradient of the sides
		m_0 = float(y_1 - y_0) / x_1 - x_0
		m_1 = float(y_2 - y_1) / x_2 - x_1
		m_2 = float(y_0 - y_2) / x_0 - x_2

		# Calculating the y-intercept of the sides
		c_0 = float(y_0 * x_1 - y_1 * x_0) / x_1 - x_0
		c_1 = float(y_1 * x_2 - y_2 * x_1) / x_2 - x_1
		c_2 = float(y_2 * x_0 - y_0 * x_2) / x_0 - x_2

		# Now calculate the x value of where the line y = m_0x
		# meets the lines y = m_1x + c_1 and y = m_2x + c_2
		x_0_intercept_1 = float(c_1) / m_0 - m_1
		x_0_intercept_2 = float(c_2) / m_0 - m_2
		y_0_intercept_1 = m_0 * x_0_intercept_1
		y_0_intercept_2 = m_0 * x_0_intercept_2

		# if neither intercept is on the boundary of the triangle, we know that
		# the triangle doesn't contain the origin
		if (not (x_0_intercept_1 <= max(x_1, x_2) and x_0_intercept_1 >= min(x_1, x_2)) and
			not (x_0_intercept_2 <= max(x_2, x_0) and x_0_intercept_2 >= min(x_2, x_0)) and
			not (y_0_intercept_1 <= max(y_1, y_2) and y_0_intercept_1 >= min(y_1, y_2)) and
			not (y_0_intercept_2 <= max(y_2, y_0) and y_0_intercept_2 >= min(y_2, y_0))):
			# neither of the x_coords of the intercept lie within the triangle
			# so we discard the triangle and move on to the next:
			triangles.remove(triangle)
			continue

		# Repeat this process for the lines y = m_1x and
		# y = m_2x
		x_1_intercept_1 = float(c_0) / m_1 - m_0
		x_1_intercept_2 = float(c_2) / m_1 - m_2
		y_1_intercept_1 = m_1 * x_1_intercept_1
		y_1_intercept_2 = m_1 * x_1_intercept_2

		if (not (x_1_intercept_1 <= max(x_0, x_1) and x_1_intercept_1 >= min(x_0, x_1)) and
			not (x_1_intercept_2 <= max(x_2, x_0) and x_1_intercept_2 >= min(x_2, x_0)) and
			not (y_1_intercept_1 <= max(y_0, y_1) and y_1_intercept_1 >= min(y_0, y_1)) and
			not (y_1_intercept_2 <= max(y_2, y_0) and y_1_intercept_2 >= min(y_2, y_0))):
			triangles.remove(triangle)
			continue

		x_2_intercept_1 = float(c_0) / m_2 - m_1
		x_2_intercept_2 = float(c_1) / m_2 - m_1
		y_2_intercept_1 = m_2 * x_2_intercept_1
		y_2_intercept_2 = m_2 * x_2_intercept_2

		if (not (x_2_intercept_1 <= max(x_0, x_1) and x_2_intercept_1 >= min(x_0, x_1)) and
			not (x_2_intercept_2 <= max(x_1, x_2) and x_2_intercept_2 >= min(x_1, x_2)) and
			not (y_2_intercept_1 <= max(y_0, y_1) and y_2_intercept_1 >= min(y_0, y_1)) and
			not (y_2_intercept_2 <= max(y_1, y_2) and y_2_intercept_2 >= min(y_1, y_2))):
			triangles.remove(triangle)
			continue

	print(len(triangles))
	return len(triangles)

FindTriangleContainment()

# Returns 









