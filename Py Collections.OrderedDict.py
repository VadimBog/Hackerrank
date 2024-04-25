# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

# Example

# Code

# >>> from collections import OrderedDict
# >>> 
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>> 
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>> 
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>> 
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for _ in range(N):  
    row = input().rsplit(maxsplit=1)
    item_name, net_price = row[0], int(row[1])
    net_price += ordered_dictionary.get(item_name, 0)
    ordered_dictionary[item_name] = net_price
    
    
for item_name, net_price in ordered_dictionary.items():
    print(item_name, net_price)