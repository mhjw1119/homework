# 맨 처음과 맨 끝만 확인해서 같을 시에 회문 검사를 실시한다. 틀리면 바로 브레이크.
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T +1):
    arr,check = list(input().split())
    N = len(check)
    count = 0
    for i in range(len(arr)):
        if arr[i] == check[0] and arr[N-1+i] == check[N-1] :
            for x in range(1,(N//2)+1) :
                if arr[i+x] == check[x] and arr[i+N-1-x] == check[N-1-x] :
                    if x == (N//2) :
                        count += 1
                else:
                    break
    result = len(arr)-((N-1)*count)

    print(f'#{test_case} {result}')