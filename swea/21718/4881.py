import sys
sys.stdin = open('input.txt','r')
def dfs (x,check) :
    real = float('inf')
    result = 0
    if x == N :
        for i in range(N):
            result += arr[check[i]][i]
        return result

    for i in range(N):
        if i not in check:
            check.append(i)
            real= min(real,dfs(x+1,check))
            check.pop()
    return real





T = int(input())
for testcase in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    check1 = []
    final = dfs(0, check1)

    print(f'#{testcase} {(final)}')