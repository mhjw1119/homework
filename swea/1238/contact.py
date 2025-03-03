import sys
sys.stdin = open('input.txt','r')

T = int(input())

for testcase in range( 1, T+1) :
    N,S = map(int,input().split())
    arr = list(map(int, input().split()))
    idx = [[] * 100]
    for i in range(0,N,2) :
        if arr[i+1] not in idx[arr[i]]:
            idx[arr[i]].append(arr[i+1])
def dfs ( s, count, road):
    if idx[s]:
        road.append(s)
        for i in idx[s] :
            dfs(i,count+1, road)
    else:
        return count