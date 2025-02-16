import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    p = [list(map(int,input())) for _ in range(N)]
    result = 0
    for high in range((N//2)+1) :   # 아래로 내려옴
        # for low in range(N//2) :
        for c in range((N//2)-high,(N//2)+high+1) :
            result += p[high][c]

    for i in range((N//2)) :  # 3 :  0 1 2
        # for low in range(N//2,-1) :
        for c in range((N//2)-i,(N//2)+i+1) :
            result += p[N-i-1][c]

    print(f'#{test_case} {result}')
