import sys
sys.stdin = open('input.txt','r')
def in_order(last) :
    if L[last] :
        if check[L[last]] == 0 :
            in_order(L[last])
    if check[last] == 0 :
        result.append(tree[last])
        check[last] = 1

    if R[last] :
        if check[R[last]] == 0:
            in_order(R[last])
    if tree[last//2] :
        if check[last//2] == 0:
            in_order(last//2)





for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str,input().split())) for _ in range(N)]
    L = [ 0 for _ in range(N+1)]
    R = [0 for _ in range(N+1)]
    tree = [[] for _ in range(N+1)]
    check = [0 for _ in range(N+1)]
    result = []
    first =0
    for i in range(N) :
        tree[int(arr[i][0])] = (arr[i][1])

        if len(arr[i]) > 2 :
            L[int(arr[i][0])] = int(arr[i][2])

        if len(arr[i]) > 3 :
            R[int(arr[i][0])] = int(arr[i][3])
    first = N
    cnt = 0
    while first != 0 :
        first //= 2
        cnt += 1
    first = 2 ** (cnt-1)
    in_order(first)
    print(f'#{tc} {"".join(result)}')