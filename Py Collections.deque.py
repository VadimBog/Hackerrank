# collections.deque()
# A deque is a double-ended queue. 
# It can be used to add or remove elements from both ends.

# Deques support thread safe, memory efficient appends and 
# pops from either side of the deque with approximately 
# the same 0(1) performance in either direction.

# Click on the link to learn more about deque() methods.
# Click on the link to learn more about various approaches 
# to working with deques: Deque Recipes.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n_op = int(input())
my_deque = deque()

for i in range(n_op):
    input_str = str(input())
    split_input = input_str.split()
    
    input_command = getattr(my_deque, split_input[0])
    input_length = len(split_input)
    
    if input_length == 1:
        input_command()
    elif input_length == 2:
        input_value = int(split_input[1])
        input_command(input_value)
            
print(*my_deque, sep=" ")