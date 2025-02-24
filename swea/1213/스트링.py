# 맨 처음과 맨 끝만 확인해서 같을 시에 회문 검사를 실시한다. 틀리면 바로 브레이크.
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for testcase in range(1, 11):
    test_case = int(input())
    check = list(input())
    arr = list(input())

    N = len(check)
    count = 0
    for i in range(len(arr)) :
        if arr[i] == check[0] and i <= len(arr) - N:
            for x in range(N) :
                if arr[i+x] != check[x] :
                    break
                else:
                    if x == N - 1:
                        count += 1


    print(f'#{test_case} {count}')