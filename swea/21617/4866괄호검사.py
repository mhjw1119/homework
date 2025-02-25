
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T +1):
    arr = input()
    stack = []
    top = -1
    result = 1
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '{' :
            stack.append(arr[i])
            top += 1
        elif arr[i] == ')' or arr[i] == '}' :
            if top == -1 :
                result = 0
                break
            if arr[i] == ')' and stack[-1] == '(':
                stack.pop()
                top -= 1
                continue
            if arr[i] == '}' and stack[-1] == '{':
                stack.pop()
                top -= 1
                continue
            result = 0
            break
    if top != -1 :
        result = 0


    print(f'#{test_case} {result}')


