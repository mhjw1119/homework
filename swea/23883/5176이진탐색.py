# import sys
# sys.stdin = open('input.txt', "r" )

def bin_search (start) :
    if start == 0:
        return
    # if tree[start*2] < tree[start] < tree[(start*2) + 1] :
    #     bin_search(start+1)
    if start * 2 < i :
        if tree[start * 2]  > tree[start] :
            tree[start],tree[start * 2 ] = tree[start*2], tree[start]
    if start * 2 + 1< i:

        if tree[start]  > tree[(start * 2) + 1 ] :
            tree[start], tree[(start * 2) + 1] = tree[(start * 2) + 1 ], tree[start]
    bin_search(start-1)



T = int(input())

for tc in range(1, 1+T) :
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1,N+1) :
        tree[i] = i
        bin_search(i//2)
    print(N//2 + 1 ,tree[N//2])
