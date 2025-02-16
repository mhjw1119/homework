
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    go = [str(input()) for _ in range(N)]
    result = 'NO'

    # check = [([0] * N) for _ in range(N)]
    # high = [([0] * N) for _ in range(N)]

    bingo = 0
    # for i in range(N) :
    #     if '.' in go[i] :
    #         continue
    #     else :
    #         if go[i].count('o') >= 5 :
    #             bingo = 1
    low = 0
    i =0
    # j = 0
    # for i in range (N) :
    #     if bingo == 1 :
    #         break
    #     low = 0
    #     for j in range (N) :
    #         if bingo == 1:
    #             break
    low_count = 0
    for i in range(N-5+1) :
        if bingo == 1 :
            break
        for j in range(N) :
            if go[j][i] == 'o' :
                low_count = 0
                for r in range(5) :
                    if go[j][i+r] == 'o' :
                        low_count += 1
                if low_count >= 5 :
                    bingo = 1
                    break
    # for i in range(N) :
    #     # print(go[i].count('o'))
    #     # print(go[i].find('o'))
    #     if bingo == 1 :
    #         break
    #     for _ in range(go[i].count('o')) :
    #         if bingo == 1:
    #             break
    #         j = go[i].find('o')
    #         if j <= N - 5:
    #             while go[i][j] == 'o':
    #
    #                 low += 1
    #
    #                 if low >= 5 :
    #                     bingo = 1
    #                     low = 0
    #                     break
    #                 # if i == N-1 :
    #                 #     break
    #                 if j == N-1 :
    #                     # i += 1
    #                     break
    #                 j += 1
    #             break

    for i in range(N-5 +1) :
        for k in range(N) :
            if bingo == 1 :
                break
            if go[i][k] == 'o' :
                high_count = 0
                for ch in range(5) :
                    if go[i+ch][k] == 'o' :
                        high_count += 1
                    else:
                        break
                if high_count >= 5 :
                    bingo = 1

    ang_count = 0

    # for i in range(N-5+1):
    #     if go[i][i] == 'o' :
    #         ang_count = 0
    #         for j in range(5) :
    #             if go[i+j][i+j] == 'o' :
    #                 ang_count += 1
    #             else:
    #                 break
    # if ang_count >= 5 :
    #     bingo = 1
    for i in range(4,N) :
        if bingo == 1:
            break

        for j in range(N-5+1) :

            if go[j][i] == 'o' :
                ang_count = 0
                for p in range(5) :
                    if go[j+p][i-p] == 'o' :
                        ang_count += 1
                    else:
                        break
                if ang_count >= 5 :
                    bingo = 1
                    break


    tng_count = 0
    for e in range(N-5+1) :
        if bingo == 1:
            break
        for i in range(N-5+1) :
            if bingo == 1 :
                break
            if go[e][i] == 'o' :
                tng_count = 0
                for j in range(5) :
                    if go[e+j][i+j] == 'o' :
                        tng_count += 1
                    else:
                        break
                if tng_count >= 5 :
                    bingo = 1
                    break

    #     if go[i][N - 1 - i] == 'o':
    #         tng_count = 0
    #         for j in range(5):
    #             if go[i + j][N - 1 - j] == 'o':
    #                 tng_count += 1
    #             else:
    #                 break
    # if tng_count >= 5:
    #     bingo = 1
    #
    # for i in range(N-5 +1) :
    #     if go[i][N-1-i] == 'o' :
    #         tng_count = 0
    #         for j in range(5):
    #             if go[i+j][N-1-j] == 'o' :
    #                 tng_count += 1
    #             else:
    #                 break
    # if tng_count >= 5 :
    #     bingo = 1

    if bingo == 1 :
        result = 'YES'

    print(f'#{test_case} {result}')


    # for i in range(N) :
    #     for j in range(N) :
    #         if go[i][j] == 'o' and go[i][j+4] == 'o' :
    #             for z in range(j+1,j+4) :
    #                 if go[i][z] == 'o' :                #가로 빙고
    #                     bingo =1
    #                     break
    #         else:
    #             break
    #
    # for i in range(N) :
    #     for j in range (N) :
    #         if go [j][i] == 'o' and  go[j][i] == 'o'



                                                #가로 검사