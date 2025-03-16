import sys
sys.stdin = open('input.txt', 'r')

def check(cnt, start):
    global result_arr

    if cnt == N:
        backup = int(''.join(map(str, arr)))
        result_arr.append(backup)
        return

    for i in range(len(arr)):
        arr[i], arr[start] = arr[start], arr[i]
        check(cnt + 1, 0)  # start+1 대신 0을 넘겨 모든 경우 탐색
        arr[i], arr[start] = arr[start], arr[i]  # 백트래킹

T = int(input())

for tc in range(1, T + 1):
    real, N = input().split()
    arr = list(map(int, real))  # 문자열을 정수 리스트로 변환
    N = int(N)
    result_arr = []

    check(0, 0)
    print(f'#{tc} {max(result_arr)}')
