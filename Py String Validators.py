# Python has built-in string validation methods for basic data. 
# It can check if a string is composed of alphabetical characters, 
# alphanumeric characters, digits, etc.

if __name__ == '__main__':
    string = input()
    methods = [
        "isalnum", "isalpha", "isdigit", "islower", "isupper"
    ]

    for method in methods:
        validations = [getattr(char, method)() for char in string]
        print(any(validations))