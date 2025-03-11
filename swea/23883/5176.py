# import sys
# sys.stdin = open('input.txt', "r" )


def bin_tree (start):
    if start == 0 :
        return
    if start*2 < N :
        if tree[start*2] > tree[start] :
            tree[start*2],tree[start] = tree[start],tree[start*2]
    if 1+(start*2) < N:
        if tree[1+(start*2)] < tree[start] :
            tree[1+(start*2)],tree[start] = tree[start],tree[1+(start*2)]
    bin_tree(start-1)



T = int(input())

for tc in range(1, 1+T) :
    N = int(input())
    tree = []
    for i in range(1,N+1) :
        tree.append(i)
    bin_tree(N//2)
    print(tree[0],tree[N//2])
