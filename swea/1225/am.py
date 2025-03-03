import sys
from collections import deque
sys.stdin = open('input.txt','r')
T = 10
for testcase in range( 1, T+1) :
    test_case = int(input())
    arr1 = deque()

    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        arr1.append(arr[i])
    i = 1
    while arr1[-1] != 0 :
        if i == 6 :
            i = 1
        first = arr1.popleft()
        first -= i
        if first <= 0:
            first = 0
            arr1.append(first)
            break
        arr1.append(first)
        i+= 1
    for i in range(8) :
        arr[i] = str(arr1[i])

    print(f'#{test_case} {" ".join(arr)}')

