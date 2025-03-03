import sys
sys.stdin = open('input.txt','r')
def dfs (x,check,s) :
    real = float('inf')
    result = 0
    global minn
    if s > minn :
        return

    if x == N :
        if minn > s :
            minn = s
        return s

    for i in range(N):
        if i not in check:
            check.append(i)
            if dfs(x+1,check,s+arr[check[-1]][x]):
                minn = min(minn,dfs(x+1,check,s+arr[check[-1]][x]))
            check.pop()
    return minn





T = int(input())
for testcase in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    minn = float('inf')
    check1 = []
    final = dfs(0, check1,0)

    print(f'#{testcase} {(final)}')