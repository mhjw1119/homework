
import sys
sys.stdin = open("input.txt", "r")

def dfs( v, N) :
    visit = [0] * (N+1)
    stack1 = []
    result = []
    while True:
        if visit[v] == 0 :
            visit[v] = 1
            result.append(str(v))
        for w in stack[v] :
            if visit[w] == 0 :
                stack1.append(v)
                v = w
                break
        else:
            if stack1:
                v = stack1.pop()
            else:
                break
    return result

T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T +1):
    V, E = map(int,input().split())
    arr = list(map(int,input().split()))
    stack = [[] for _ in range(V+1)]
    for i in range(0,len(arr),2) :
        stack[arr[i]].append(arr[i+1])
        stack[arr[i+1]].append(arr[i])
    result1 = dfs(1,V)
    print(f'#{test_case} {"-".join(result1)}')



