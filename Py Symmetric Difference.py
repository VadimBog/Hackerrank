# Objective
# Today, we're learning about a new data type: sets.

# Concept

# If the inputs are given on one line separated by a character (the delimiter), 
# use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. 
# To specify that comma is the delimiter, use string.split(','). 
# For this challenge, and in general on HackerRank, space will be the delimiter.

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

dif_set1 = a.difference(b)
dif_set2 = b.difference(a)
dif_list = list(dif_set1.union(dif_set2))
for i in sorted(dif_list):
    print(i)