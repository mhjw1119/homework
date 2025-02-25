# # 맨 처음과 맨 끝만 확인해서 같을 시에 회문 검사를 실시한다. 틀리면 바로 브레이크.
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T +1):
    arr = list(input())
    stack = []
    N = len(arr)
    stack.append(arr[0])
    top = 0
    for i in range(1,N) :
        if top != -1 :
            if stack[-1] == arr[i] :
                stack.pop()
                top -= 1
            else:
                stack.append(arr[i])
                top += 1
        else:
            stack.append(arr[i])
            top += 1

    print(f'#{test_case} {len(stack)}')

