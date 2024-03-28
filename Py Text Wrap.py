# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    counter = max_width
    new_string = ''
    for i in string:
        if counter > 0:
            new_string += i
            counter -= 1
        else:
            new_string = new_string + '\n' + i
            counter = max_width - 1
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)