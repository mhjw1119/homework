import sys
sys.stdin = open('input.txt','r')

def node1 (n):
    if n == 1 :
        return
    if node[n//2] == 0 :
        if n//2 == (n-1) // 2 :
            node[(n//2)] = node[n] + node[n-1]
            node1(n//2)
        else:
            node[n // 2] = node[n]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    node = [0] * (N+1)

    for i in arr :
        node[i[0]] = i[-1]

    node1(N)
    print(node[L])