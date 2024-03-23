# In Python, a string can be split on a delimiter.

def split_and_join(line):
    list = line.split(" ")
    mod_string = "-".join(list)
    return mod_string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

    


