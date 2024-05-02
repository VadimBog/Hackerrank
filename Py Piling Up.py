# Enter your code here. Read input from STDIN. Print output to STDOUT
def pick_cube(cubes):
    return 0 if cubes[0] > cubes[-1] else -1

test_count = int(input())
for _ in range(test_count):
    cube_num = int(input())
    cubes = list(map(int, input().split()))
    vert_stack = []
    
    # Pick the first cube
    vert_stack.append(cubes.pop(pick_cube(cubes)))
    
    # Build the stack
    while len(cubes) > 0:
        idx = pick_cube(cubes)
        if cubes[idx] > vert_stack[-1]:
            print('No')
            break
        
        vert_stack.append(cubes.pop(idx))
    
    if len(cubes) == 0:
        print('Yes')