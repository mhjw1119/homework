
import sys
sys.stdin = open("input.txt", "r")

'''
스택이 필요한 dfs이다
모든 배열을 다 돌며 델타로 상하좌우에 큰 값을 찾는다.
큰 값을 찾으면 dfs함수를 실행한다.
dfs함수는 상하좌우로 다시 델타를 돌면서 자신보다 큰 값을 찾는다.
이 때 한 번 갔던 곳은 다시 가지 않도록 인덱스를 확인하여 간 곳이면 가지 않는다.
순회가 끝나고 지금 까지 찾은 최대 등산로의 길이보다 1 작은 경우 마지막 위치에서
마지막 위치 - 1 + 

'''
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs (idx,check,sp,count) :
    y,x = idx
    check[y][x] = 1
    result = count
    back = 0
    for delta in range(4) :
        ny = y + dy[delta]
        nx = x + dx[delta]
        if -1 < ny < N and -1 < nx < N :
            if arr[y][x] > arr[ny][nx] and check[ny][nx] != 1 :
                idx = [ny,nx]
                result = max(result,dfs(idx,check,sp,count+1))
            if sp == 1 and check[ny][nx] != 1 :
                if arr[ny][nx] - K < arr[y][x] :
                    for fi in range(1,K+1) :
                        if arr[ny][nx] - fi < arr[y][x] :

                            break
                    idx = [ny, nx]
                    sp = 0
                    back = arr[ny][nx]
                    arr[ny][nx] -= fi
                    result = max(dfs(idx, check, sp, count + 1), result)
                    arr[ny][nx] = back
                    sp = 1
    check[y][x] = 0
    return result

T = int(input())

for test_case in range(1,T+1) :
    N, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    real = 0
    top = 0
    max_idx = []

    for aa in range(N) :
        top = max(max(arr[aa]),top)

    for i in range(N) :
        for j in range(N) :
            check1 = [[0] * N for _ in range(N)]
            road = [i,j]
            first = 1
            first_count = 0
            if arr[i][j] == top :
                real = max(dfs(road,check1,first,first_count),real)
            else:
                continue
    print(f'#{test_case} {real+1}')