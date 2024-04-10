# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    _ = input()

    A = set(map(int, input().split()))

    _ = input()

    B = set(map(int, input().split()))

    print(A.issubset(B))