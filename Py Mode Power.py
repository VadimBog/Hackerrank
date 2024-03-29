# So far, we have only heard of Python's powers. Now, we will witness them!

# Powers or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:

# >>> pow(a,b) 
# or

# >>> a**b
# It's also possible to calculate a^b mad m.

# >>> pow(a,b,m)  
# This is very helpful in computations where you have to print the resultant % mod.

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))

# input:
# 3
# 4
# 5

# output:
# 81
# 1