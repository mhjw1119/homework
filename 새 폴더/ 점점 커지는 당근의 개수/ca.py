
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = 0
    count = 0
    real_result = 0
    for i in range(N) :
        if result < arr[i] :
            result = arr[i]
            count += 1
        else:
            real_result = max(count,real_result)
            count = 1
            result = arr[i]

    print(f'#{test_case} {count}')

