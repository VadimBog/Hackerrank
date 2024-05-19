# .difference()
# The tool .difference() returns a set with all 
# the elements from the set that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, 
# but it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).

# Task
# Students of District College have a subscription to English and French newspapers. 
# Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, 
# and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
# and one set has subscribed to the French newspaper. 
# Your task is to find the total number of students who have subscribed to only English newspapers.

# Input Format

# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Enter your code here. Read input from STDIN. Print output to STDOUT

a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
result=len(b.difference(d))
print(result) 