# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dr = 0
    i,j = 0

    while i*j != N*N :
        for i in range
        ny = j+dy[dr]
        nx = i+dx[dr]
        if -1 < nx < N and -1 < ny < N