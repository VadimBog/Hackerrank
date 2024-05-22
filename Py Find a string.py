# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.


# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

import re
def count_substring(string, sub_string):
    pattern = re.compile(f"(?=({sub_string}))")
    matches = list(pattern.findall(string))
    return len(matches)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)