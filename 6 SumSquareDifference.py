# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.

# Notice that the difference is just sum of all the cross terms from the square of the sum.
# So we can form a grid of the summands as follows:
# x 1  2  3  4  5...
# 1    2  3  4  5
# 2 2     6  8  10
# 3 3  6     12 15
# 4 4  8  12    20
# 5 5  10 15 20  
# .
# .
# .
#
# But then notice that the sum of all the values in the grid is just 2 times the sum of all the values
# in the upper right segment.
# So we iterate over that segment:

def FindSumSquareDifference():
      sum = 0

      for i in range(1, 101):
            for j in range(i + 1, 101):
                  sum += i * j

      print 2 * sum
      return 2 * sum

FindSumSquareDifference()
# Returns 25164150