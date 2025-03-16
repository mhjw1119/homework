import sys
sys.stdin = open('input.txt', "r" )


def bin_tree (start):
    if start == 0 :
        return
    if start*2 < N :
        if result[start*2] > result[start] :
            result[start*2], result[start] = result [start], result[start*2]
    if 1+(start*2) < N:
        if result[1+(start*2)] < result[start] :
            result[1+(start*2)],result[start] = result[start], result[1+(start*2)]
    bin_tree(start-1)




T = int(input())

for tc in range(1, 1+T) :
    N = int(input())
    tree = list(range(1,N+1))
    result = []
    result.append(tree[N//2])
    for i in range(N) :
        if i == N//2 :
            continue
        result.append(tree[i])
        bin_tree(i//2)
    print(result[0],result[N//2])
