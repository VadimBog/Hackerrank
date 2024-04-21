# The defaultdict tool is a container in the collections class of Python. 
# It's similar to the usual dictionary (dict) container, 
# but the only difference is that a defaultdict will have a default value if that key has not been set yet. 
# If you didn't use a defaultdict you'd have to check to see if that key exists, 
# and if it doesn't, set it to what you want.
# For example:

# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
# This prints:

# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])

# Input Format

# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.

# Output Format

# Output m lines.
# The i line should contain the 1-indexed positions of the occurrences of the i word separated by spaces.

# Sample Input

# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b
# Sample Output

# 1 2 4
# 3 5


from collections import defaultdict

def group_positions(n, m, group_a, group_b):
    positions = defaultdict(list)

    for i, word in enumerate(group_a, start=1):
        positions[word].append(i)

    for word in group_b:
        if word in positions:
            print(*positions[word])
        else:
            print(-1)

n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

group_positions(n, m, group_a, group_b)