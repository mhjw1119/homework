
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N) ]

    # def check ( num, k ) :
    low_count = 0
    high_count = 0
    result = 0
        # for k in range(k//2) :
        #     if num[i] == num[i+(k//2)] :
        #         count += 1
        #     else:
        #         break
        # if count ==
    for i in range(N) :
        for j in range(N) :
            if j < N - K -1 :
                for q in range(K // 2):
                    if puzzle[i][j+q] == puzzle[i][j+K-1-q] :
                        if j == 0 or puzzle[i][j-1] == 0 :
                        # 가로 탐색중 왼쪽에 1이 없거나 벽일때
                            if j == N-1 or puzzle[i][j+K-1] == 0 :
                                #가로 탐색중 오른쪽에 1이 없거나 벽일때
                                low_count += 1
                if low_count == K//2 :
                    result += 1
            for q in range(K // 2):
                if puzzle[j+q][i] == puzzle[j+K-1-q][i] :
                    if j == 0 or puzzle[i][j-1] == 0 :
                    # 가로 탐색중 왼쪽에 1이 없거나 벽일때
                        if j == N-1 or puzzle[i][j+K-1] == 0 :
                            #가로 탐색중 오른쪽에 1이 없거나 벽일때
                            high_count += 1
            if high_count == K//2 :
                result += 1


