#  2의 인덱스 값에서 시작한다.
#  양 옆으로 방향 전환이 없으면 상승, 방향 전환이 있으면 경로 바꾸기
#  이 때 맨 끝에 닿는 경우를 고려해야한다.
#  왼쪽으로 갔다가 다시 돌아오는 경우를 막아야한다.  전환 하면 카운트를 하나 올린다. 이 때 곧 바로 전환하면 카운트가 2가 된다. 그러면 못 오게 한다
#  그렇게 계속 순회 해서 y의 값이 -99일 때 까지 간다.

import sys
sys.stdin = open("in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ladder = [list(map(int, input().split()))for _ in range(100)]
    y = -1
    x = ladder[-1].index(2)
    count = 0
    dx = [-1,1,0]
    dy = [0,0,-1]
    while y != -99 :
        r =0

        for i in range(3) :                 # 왼쪽에 1이 있으면 1쪽으로 한칸 간다
            nx = dx[i] + x
            ny = dy[i] + y

            if  nx < 0 or nx > 99 :  #왼쪽 인덱스 값은  x>0 이어야하고 오른쪽은 x<n-1이어야한다
                continue

            if ladder[nx][ny] == 1 :
                x = nx
                y = ny
    print(x)

    # print(f'#{test_case} {max(result)}')
