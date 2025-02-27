
import sys
sys.stdin = open("input.txt", "r")

'''
그냥 괄호 검사해서 괄호가 바로 닫히면 레이저, 안닫히고 있다가 닫히면 쇠막대기 끊기는거
결국 이 문제는 괄호가 바로 닫혔을때 (레이저가 발사 됐을 때) , 
스택 안에 괄호가 몇 개 있는지 확인하는 문제다.(몇 개의 쇠막대기가 잘리는지)
'''
def check (a) :
    stack = []
    count = 0
    result = 0
    for i in range(len(a)) :
        if a[i] == '(' :
            stack.append(a[i])
        if a[i] == ')' :
            if a[i-1] == '(' :
                result += len(stack)-1
            else:
                result += 1
            stack.pop()
    return result






T = int(input())

for testcase in range(1,T+1) :
    arr = list(input())
    print(f'#{testcase} {check(arr)}')



