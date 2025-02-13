import sys
sys.stdin = open("input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N) :
        A[i],B[i] = map(int,input().split())
    P = int(input())
    PP = [0] * P
    for i in range(P):
        PP[i] = int(input())
    result = [0] * 5000
    real_result = [0] * P

    for i in range(N) :
        for j in range(A[i],B[i]+1) :
            result[j-1] += 1

    for i in range(P) :
        real_result[i] = result[PP[i]-1]

    print(f"#{test_case} {' '.join(map(str,real_result))}")