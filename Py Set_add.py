# If we want to add a single element to an existing set, we can use the .add() operation.
# It adds the element to the set and returns 'None'.

# Example

# >>> s = set('HackerRank')
# >>> s.add('H')
# >>> print s
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# >>> print s.add('HackerRank')
# None
# >>> print s
# set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

N = int(input())
s = set()
for i in range(N):
    ch = input()
    s.add(ch)
    
print(len(s))