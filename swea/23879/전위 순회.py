def first ( f ) :
    result.append(str(f))
    check[f] = 1

    for nd in node[f] :
        if check[nd] != 1 :
            first(nd)
    return

V = int(input())
arr = list(map(int, input().split()))
node = list([] for _ in range(V+1))
for i in range(0,len(arr),2) :
    node[arr[i]].append(arr[i+1])
result = []
check = [0] * (V+1)
first(1)
print(" ".join(result))




