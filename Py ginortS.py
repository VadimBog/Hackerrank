# You are given a string S.
# S contains alphanumeric characters only.
#  Your task is to sort the string S in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string S.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def custom_sort(S):
    sorted_chars = sorted(S, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
    return ''.join(sorted_chars)

S = input()

sorted_string = custom_sort(S)
print(sorted_string)