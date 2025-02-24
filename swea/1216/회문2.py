# 맨 처음과 맨 끝만 확인해서 같을 시에 회문 검사를 실시한다. 틀리면 바로 브레이크.
import sys
sys.stdin = open("input.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    testcase = int(input())

    arr = [list(input()) for _ in range(100)]
    real_result = 0
    for i in range(100) :
        for j in range(100) :
            for high in range(100):
                if arr[i][j] == arr[99-high][j]:
                    for count in range(49-high):
                        if arr[i+count][j] == arr[99-high-count+i][j] :
                            if count == 49 - high -1 :
                                result = (count*2) +2
                                real_result = max(result, real_result)
                        else:
                            break

                else:
                    continue
            for low in range(100) :
                if arr[i][j] == arr[i][99-low]:
                    for count in range(49-low):
                        if arr[i][j+count] == arr[i][99-count] :
                            if count == 49 - low -1 :
                                result = (count*2) +2
                                real_result = max(result, real_result)
                        else:
                            break
    print(f'#{testcase} {real_result}')