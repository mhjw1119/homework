import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,K = map(int,input().split())
    box = [0] * 12
    for i in range(12) :
        box[i] = i + 1
    result = 0

    for i in range(1<<12):
        part = []
        for j in range(12) :
            if i & (1<<j) :
                part.append(box[j])
                if len(part) == 3 and sum(part) == 6 :
                    result += 1

    print(result)
