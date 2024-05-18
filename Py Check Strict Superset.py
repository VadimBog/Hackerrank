# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.

# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Input Format

# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int, input().split()))
c=0
for i in range(int(input())):
    st = set(map(int, input().split()))
    
    if len(st.difference(a))==0 and (len(a)-len(st))>=1:
        output ='True'
    else:
        c+=1

if c==0:
    print(output)
else:
    print('False')

