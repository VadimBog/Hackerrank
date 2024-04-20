# You are given an integer, N. 
# Your task is to print an alphabet rangoli of size N. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []

    # Build each line of the rangoli pattern
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append((s[::-1] + s[1:]).center(4*size-3, '-'))

    # Print the rangoli pattern
    print('\n'.join(lines[:0:-1] + lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)