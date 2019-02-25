# How many taxicab routes are there through a 20×20 grid?

# In the case of the 2x2 grid, you can move right exactly twice
# and down exactly twice. So the number of paths is just the number
# of unique combinations of L, L, D, D (i.e. 4C2 = 6 paths)

# So for the 20x20 grid the amount of paths is just the number of unique
# combinations of 20 L's and 20 D's (i.e. 40C20 paths)

# Returns 137846528820 (40C20)