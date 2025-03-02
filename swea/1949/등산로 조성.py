
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

# def dfs (check, idx, count,sp) :
#     y, x = idx
#     check[y][x] = 1
#     count += 1
#     result = count
#     for i in range(4) :
#         ny = dy[i] + y
#         nx = dx[i] + x
#         if -1 < ny < N and -1 < nx < N :
#             if arr[y][x] <  arr[ny][nx] and check[ny][nx] != 1 :
#                 idx = [ny,nx]
#                 result = max(result,dfs(check,idx,count,sp))
#                 if sp != 0 :
#                     for j in range(4) :
#                         nny = y + dy[j]
#                         nnx = x + dx[j]
#                         if -1 < nnx < N and -1 < nny < N :
#                             if arr[y][x] - K  < arr[nny][nnx] and check[nny][nnx] != 1 :
#                                 idx = [nny,nnx]
#                                 sp = 0
#                                 result = max(result, dfs(check, idx, count, sp))
#                                 sp = 1
#                                 check = [[0] * N for _ in range(N)]
#
#     return result
def dfs(check, path, count):
    if not path:
        return count  # 경로가 없으면 현재 count 반환

    y, x = path[-1]
    check[y][x] = 1  # 방문 표시

    max_count = count  # 최대 등산로 길이 저장

    for i in range(4):  # 4방향 탐색
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < N and 0 <= nx < N:  # 배열 범위 체크
            if arr[y][x] < arr[ny][nx] and check[ny][nx] == 0:  # 더 높은 지형만 탐색
                path.append([ny, nx])
                max_count = max(max_count, dfs(check, path, count + 1))  # 재귀 호출 후 최댓값 갱신
                path.pop()  # 백트래킹

    check[y][x] = 0  # 백트래킹 (방문 초기화)
    return max_count  # 항상 반환하도록 수정


T = int(input())

for test_case in range(1,T+1) :
    N, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    real = 0
    for i in range(N) :
        for j in range(N) :
            first_count = 0
            check1 = [[0] * N for _ in range(N)]
            road = [[i,j]]
            result = dfs(check1,road,first_count)
    print(f'#{test_case} {real}')





