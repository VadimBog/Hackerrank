# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_to_set = set(arr)
    arr2 = sorted(list(arr_to_set))
    print(arr2[-2])

# Output:
    # n = 5
    # 2 3 6 6 5
    # 5
    # n = 10
    # 2 3 6 6 5 5 5 5 5 5
    # 6
    # n = 15
    # 2 3 6 6 5 5 5 5 5 5 5 5 5 5 5
    # 6
    # n = 20
    # 2 3 6 6