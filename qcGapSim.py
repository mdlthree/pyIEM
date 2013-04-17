import numpy as np
#help(np.random.randn)

# This example is from the notes of IEM 5103 (chapter 11, slide 21)
#   part A has a mean of 5 and a range of +/- 0.3 
#   which we can convert to a SD by dividing by Z(a = 0.05) or 1.96

partA = (5,0.3/1.96)
#  which we store as a tuple (like an immutable array)
partB = (2,0.2/1.96)
partC = (10, 0.1/1.96)

partA, partB, partC
# output parameters

# now let us create 3 arrays of normally distributed values
#   remember this implementation uses 4*L elements
# A = u + Z*SD, transformation from N(0,1) to N(u,s^2)
L = 1000000 # 1 million
#L = 10000000 # 10 million
#L = 50000000 # 50 million

A = partA[0] + np.random.randn(L)*partA[1]
B = partB[0] + np.random.randn(L)*partB[1]
C = partC[0] + np.random.randn(L)*partC[1]
type(A)

# gap = partC - (partA + partB)
# we will use special functions call ufuncs (universal function)
#   they are specially implemented C functions to process ndarray's
#   in a vectorized (parallel) fashion
gap = np.subtract(C, np.add(A,B))

gap[:10]
# intro to slices

gap[-10:]
# what is this one?

gap[L-1]
#proof that the last one is right

# compute some statistics
#   should work out to
#   u = 10 - 2 - 5 = 3
print np.mean(gap), np.std(gap)
