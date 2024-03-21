if __name__ == '__main__':
    N = int(input())
    list = []
    
    for i in range(N):
        comand = input().split()
        if comand[0] == 'insert':
            list.insert(int(comand[1]), int(comand[2]))
        elif comand[0] == 'print':
            print(list)
        elif comand[0] == 'remove':
            list.remove(int(comand[1]))
        elif comand[0] == 'append':
            list.append(int(comand[1]))
        elif comand[0] == 'sort':
            list.sort()
        elif comand[0] == 'pop':
            list.pop()
        elif comand[0] == 'reverse':
            list.reverse()