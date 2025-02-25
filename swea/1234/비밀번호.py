# 맨 처음과 맨 끝만 확인해서 같을 시에 회문 검사를 실시한다. 틀리면 바로 브레이크.
import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T +1):
    N,arr = input().split()
    arr1 = []
    for i in range(int(N)):
        arr1.append(arr[i])
    i = 0
    check = []
    while i != len(arr1)-1 :
        if arr1[i] == arr1[i+1] :
            arr1.pop(i)
            arr1.pop(i)
            i = 0
        else:
            i += 1
    print(f'#{test_case} {"".join(arr1)}')

