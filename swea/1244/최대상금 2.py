
import sys
sys.stdin = open('input.txt', 'r')
def check (cnt, start) :
    global result
    global result_arr
    backup = ''
    if cnt == N :
        for i in arr :
            backup += str(i)
        result_arr.append(int(backup))
        return

    if start >= len(arr) :
        # check(cnt,0)
        # if max_arr == arr[0]:
        for i in range(len(arr)):
            check(cnt, i)
        return

    for i in range(len(arr)):
        if i == start:
            continue
        arr[i], arr[start] = arr[start], arr[i]
        check(cnt + 1,start+1)
        arr[i], arr[start] = arr[start], arr[i]





T = int(input())

for tc in range(1,T+1):

    real,N =  map(str,input().split())
    arr = []
    result_arr = []
    N = int(N)
    visit = [0] * (len(arr) + 1)
    result = 0
    for q in real:
        arr.append(int(q))
    max_arr = 0
    max_arr = max(arr)
    check(0,0)
    print(f'#{tc} {max(result_arr)}')
