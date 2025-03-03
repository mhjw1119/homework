import sys
sys.stdin = open('input.txt','r')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    testca = int(input())
    arr = [list(input()) for _ in range(100)]


    def bfs ( idx ):
        q = []
        check = [[False] * 100 for _ in range(100)]
        y,x = idx
        q.append(idx)
        check[y][x] = True

        while q :
            y,x = q.pop()
            if arr[y][x] == '3' :
                return 1
            for dr in [[1,0],[0,1],[0,-1],[-1,0]] :
                ny = dr[0] + y
                nx = dr[-1] + x
                if -1 < ny < 100 and -1 < nx < 100 :
                    if check[ny][nx] != 1 and arr[ny][nx] != 1 :
                        q.append([ny,nx])
                        check[ny][nx] = True
        return 0


    first_idx = [1,1]
    result = bfs(first_idx)
    print(f'#{testca} {result}')




