import sys
sys.stdin = open('input.txt', "r" )


def in_order(p):
    c = p * 2
    if p < N:
        in_order(c)
        arr[p] = que.pop(0)
        in_order(c + 1)
    elif p == N:
        in_order(c)
        arr[p] = que.pop(0)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 1)
    que = list(range(1, N + 1))
    in_order(1)
    print(f'#{tc} {arr[1]} {arr[N // 2]}')

# import sys
# sys.stdin = open('input.txt', "r" )
#
# def bin_search (start) :
#     if start == 0:
#         return
#     # if tree[start*2] < tree[start] < tree[(start*2) + 1] :
#     #     bin_search(start+1)
#     if start * 2 < i :
#         if tree[start * 2]  > tree[start] :
#             tree[start],tree[start * 2 ] = tree[start*2], tree[start]
#     if (start * 2) + 1< i:
#
#         if tree[start]  > tree[(start * 2) + 1 ] :
#             tree[start], tree[(start * 2) + 1] = tree[(start * 2) + 1 ], tree[start]
#     bin_search(start-1)
#
#
#
# T = int(input())
#
# for tc in range(1, 1+T) :
#     N = int(input())
#     tree = [[] for _ in range(N+1)]
#     for i in range(1,N+1) :
#         tree[i] = i
#         bin_search(i//2)
#     print(tree[1] ,tree[N//2])
