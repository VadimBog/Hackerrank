# We have seen the applications of union, intersection, difference and symmetric difference operations, 
# but these operations do not make any changes or mutations to the set.

# We can use the following operations to create mutations to a set:
# .update() 
# .intersection_update()
# .difference_update() 
# .symmetric_difference_update()

# TASK

# You are given a set A and N number of other sets. 
# These N number of sets have to perform some specific mutation operations on set A.

# Your task is to execute those operations and print the sum of elements from set A.

# Input Format

# User
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2 * N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

# Enter your code here. Read input from STDIN. Print output to STDOUT
A_el = int(input())
A_set = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    operation_name, other_set_length = input().split()
    other_set_length = int(other_set_length)
    other_set = list(map(int, input().split()))
    if operation_name == 'update':
        A_set.update(other_set)
    elif operation_name == 'intersection_update':
        A_set.intersection_update(other_set)
    elif operation_name == 'difference_update':
        A_set.difference_update(other_set)
    else:
        A_set.symmetric_difference_update(other_set)
        
print(sum(A_set))