import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    chart = [list(map(int, input().split())) for _ in range(9)]
    check = [0] * 9
    fail =0
    result = 0
    # for i in range(0,9,3) :                         # 세로 값
    #     if fail == 1:
    #         break
    #     for j in range(0,9,3) :                     # 가로 값
    #         if fail == 1 :
    #             break
    #         for b in range(3) :             # 박스 체크
    #             for bb in range(3):
    #                 check[chart[i+b][j+bb]-1] = chart[i+b][j+bb]
    #         if 0 in check :
    box_count = 0
    while box_count != 9 :
        for i in range(0,9,3) :
            for j in range(0,9,3) :
                for high in range(3) :
                    for low in range(3) :
                        check[(chart[i+high][j+low])-1] = chart[i+high][j+low]
                if 0 in check :
                    fail = 1
                    box_count = 9
                check = [0] * 9
        # high_check = [0] * 9
        for low in range(9) :
            high_check = [0] * 9
            for high in range(9) :
                high_check[chart[high][low]-1] = chart[high][low]
            if 0 in high_check :
                fail = 1
                box_count = 9
                break

        for high in range(9):
            low_check = [0] * 9
            for low in range(9):
                low_check[chart[high][low]-1] = chart[high][low]
            if 0 in low_check:
                fail = 1
                box_count = 9
                break
        break
    if fail == 0 :
        result = 1
    print(f'#{test_case} {result}')





    #             fail = 1
    #             break
    #         check = [0] * 9
    # check = [0] * 9
    # if fail != 1 :
    #     for i in range(9) :           #   가로 검사
    #         check = [0] * 9
    #         for j in range(9):
    #
    #             check[chart[i][j]-1] = chart[i][j]
    #         for z in range(9):
    #             if check[z] != z+1 :
    #                 fail = 1
    #
    #                 break
    # if fail != 1 :
    #     for i in range(9) :
    #         check = [0] * 9     #   가로 검사
    #         for j in range(9):
    #
    #             check[chart[j][i]-1] = chart[i][j]
    #         for z in range(9):
    #             if check[z] != z + 1:
    #                 fail = 1
    #                 break
    # if fail != 1:
    #     result = 1
    # else:
    #     result = 0
    # print(f'#{test_case} {result}')