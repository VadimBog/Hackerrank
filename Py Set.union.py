# .union()

# The .union() operator returns the union of a set and the set of elements in an iterable.
# Sometimes, the | operator is used in place of .union() operator, 
# but it operates only on the set of elements in set.
# Set is immutable to the .union() operation (or | operation).

n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

s_union = s1.union(s2)
counter = 0
for i in s_union:
    counter += 1
    
print(counter)