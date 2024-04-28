# You are given n words. Some words may repeat. 
# For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. 
# See the sample input/output for clarification.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())

words = []

for i in range(n):
    word = input()
    words.append(word)

a = Counter(words)

b = list(a.values())

print(len(b))
print(*b)