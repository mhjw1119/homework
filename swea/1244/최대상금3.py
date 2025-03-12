import sys
sys.stdin = open('input.txt', 'r')

def check(cnt, start):
    global max_value  # 최댓값 추적

    if cnt == N:  # 교환 횟수가 N이면 최대값 업데이트
        max_value = max(max_value, int(''.join(map(str, arr))))
        return

    for i in range(start, len(arr)):  # 중복 탐색 방지
        arr[i], arr[start] = arr[start], arr[i]
        check(cnt + 1, start + 1)
        arr[i], arr[start] = arr[start], arr[i]  # 원래대로 복구 (백트래킹)

T = int(input())

for tc in range(1, T + 1):
    real, N = input().split()
    arr = list(map(int, real))  # 문자열을 숫자 리스트로 변환
    N = int(N)

    max_value = 0  # 최댓값 저장 변수 초기화
    check(0, 0)

    print(f'#{tc} {max_value}')
