import sys
sys.stdin = open("input.txt",'r')

dr = [[0,1],[1,0],[0,-1],[-1,0]]
# dr = [[1,1],[-1,-1]]

def find_x ():
    for y in range(N):
        for x in range(N):
            if arr[y][x] == "X":
                return [y,x]
def dfs( idx, cnt, k, r_dr):
    global result

    y, x = idx

    if cnt > result :
        return

    if arr[y][x] == 'Y' :
        result = min(result, cnt)

        return

    for i in range(4):
        ny = dr[i][0] + y
        nx = dr[i][1] + x

        if -1 < ny < N and -1 < nx < N :
            turn = min(abs(r_dr - i), 4 - abs(r_dr - i))
            if turn == 3:
                turn = 1
            if check[ny][nx] != 1 :
                if arr[ny][nx] == 'T' :
                    if k > 0 :
                        check[ny][nx] = 1
                        dfs([ny, nx], cnt + 1 + turn, k-1,i)
                        check[ny][nx] = 0

                    else:
                        continue
                else:
                    check[ny][nx] = 1
                    dfs([ny,nx],cnt+1+turn, k,i)
                    check[ny][nx] = 0



T = int(input())



for tc in range( 1, T+1 ):
    N, K = map(int, input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    check = [[0]*N for _ in range(N)]
    result = 100000000000000000000000000000000000000000000000000
    dr_cnt = 0

    yy,xx = find_x()
    # check[yy][xx] = 1
    dfs([yy,xx],0,K,3)

    if result == 100000000000000000000000000000000000000000000000000 :
        result = -1
    print(f'#{tc} {result}')


