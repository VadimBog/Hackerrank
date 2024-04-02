# Errors detected during execution are called exceptions.

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())  # Convert the first input to an integer
for _ in range(T):  # Iterate T times
    try:
        a, b = map(str, input().split())
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
