# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and
# outputs the standard deviation of the lengths of the strings. Return
# float('NaN') if L is empty.

# Recall that the standard deviation is computed by this equation:

# where:

#  is the mean of the elements in X.

#  means the sum of the quantity  for t in X.

# That is, for each element (that we name t) in the set X, we compute the
# quantity . We then sum up all those computed quantities.

# N is the number of elements in X.

# Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.

# Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'],
# stdDevOfLengths(L) should return 1.8708.

# If you want to use numpy arrays, you should import numpy as np and use
# np.METHOD_NAME in your code.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import numpy as np
    import math

    if len(L) == 0:
        return float('NaN')

    lengths = [len(x) for x in L]

    mean = math.fsum(lengths)/len(lengths)

    return math.sqrt(sum([(x - mean)**2 for x in lengths])/float(len(L)))