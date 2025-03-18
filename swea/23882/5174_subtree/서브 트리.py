def check ( start) :
    pass



T = int(input())

for tc in range(1, T+1 ) :
    E,N = map(int, input().split())
    backup = list(map(int, input().split()))
    node = [[0] * (E + 1)]
    print(node)
    for i in range(0,len(backup),2) :
        if node[backup[i]] == 0 :
            node[backup[i]] = backup[i+1]
        else :
            node[backup[i]].append(backup[i + 1])
    print(node)
