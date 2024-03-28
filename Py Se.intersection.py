# .intersection()

# The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
# Sometimes, the & operator is used in place of the .intersection() operator, 
# but it only operates on the set of elements in set.
# The set is immutable to the .intersection() operation (or & operation).

n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

s_intersection = s1.intersection(s2)
counter = 0
for i in s_intersection:
    counter += 1
    
print(counter)