
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    card = list(input())
# love you
    backup = [0] * 10
    for i in range(6) :
        backup[int(card[i])] += 1
    end = 0
    count = 0
    result = 0
    while count != 2 :
        flag = 0
        if end == 10 :
            break
        if backup[end] > 0 :
            if end < 7 :
                if backup[end+1] > 0 and backup[end+2]> 0 :
                    backup[end] -= 1
                    backup[end + 1] -= 1
                    backup[end + 2] -= 1
                    count += 1
                    end = 0
                    flag = 1

                # else :
            if backup[end] >= 3 :
                backup[end] -= 3
                count += 1
                end = 0
                flag = 1
            if flag == 0:
                end += 1
        else:
            end += 1
    if count == 2 :
        result = 'true'
    else :
        result = 'false'
    print(f'#{test_case} {result}')