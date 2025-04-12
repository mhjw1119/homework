import sys
sys.stdin = open("input.txt","r")

T = 10

def bfs():
    check_list = [[0] * 16 for _ in range(16)]
    que = []
    que.append([1, 1])

    while que :
        y, x = que.pop(0)
        check_list[y][x] = 1
        if arr[y][x] == 3:
            return 1


        for dr_y, dr_x in [0,1],[1,0],[0,-1],[-1,0] :
            ny = dr_y + y
            nx = dr_x + x
            if -1 < ny < 16 and -1 < nx < 16:
                if check_list[ny][nx] or arr[ny][nx] == 1:
                    continue
                que.append([ny, nx])
    return 0




for tc in range( 1, T+1 ) :
    test_case = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    print(f'#{test_case} {bfs()}')
