import sys
sys.stdin = open('input.txt','r')

T = int(input())

def dfs(s,g) :
    if s == g :
        return 1

    for ad in adj[s] :
        if dfs(ad,g):
            return 1
    return 0




for testcase in range(1,T+1) :
    V, E = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    for i in arr :
        adj[i[0]].append(i[-1])

    print(dfs(S,G))


