'''
dfs문제다 !
a를 선택할건지 b를 선택할건지 선택지를 고르는 걸로 부분집합을 구하면된다.
재귀함수를 활용한다.

'''
import sys
sys.stdin = open("input.txt", "r")

def check ( n, no ) :
    global result
    a = [20,10]
    b = [20,20]




    # if n == 0 :
    #     n = stack.pop()
    #     return check(n,n)
    #
    #
    # if n >= b and no != b:
    #     n -= b
    #     stack.append(b)
    #     result += 1
    #     return check(n,0)
    #
    # if n >= a and no != a :
    #     n -= a
    #     stack.append(a)
    #     result += 1
    #     return check(n,0)
    # if len(stack) == 0 :
    #     return result
    # else:
    #     back = stack.pop()
    #     n += back
    #     return check(n,back)



T = int(input())

for testcase in range(1,T+1) :
    result = 0
    stack = []
    N = int(input())
    print(check(N,0))