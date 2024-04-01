# itertools.product()

# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

# Input reading
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute cartesian product
cartesian_product = list(product(A, B))

# Print cartesian product
for item in cartesian_product:
    print(item, end=" ")