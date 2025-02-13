'''
각 단어에 맞는 진짜
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    testcase, N = data.split()
    testcase = int(testcase[1:])
    N = int(N)
    org = (input().split())
    backup = [0] * N
    result = [0] * N

    number = {}
    number["ZRO"] = 0
    number["ONE"] = 1
    number["TWO"] = 2
    number["THR"] = 3
    number["FOR"] = 4
    number["FIV"] = 5
    number["SIX"] = 6
    number["SVN"] = 7
    number["EGT"] = 8
    number["NIN"] = 9

    reverse_number = {}
    reverse_number[0] = "ZRO"
    reverse_number[1] = "ONE"
    reverse_number[2] = "TWO"
    reverse_number[3] = "THR"
    reverse_number[4] = "FOR"
    reverse_number[5] = "FIV"
    reverse_number[6] = "SIX"
    reverse_number[7] = "SVN"
    reverse_number[8] = "EGT"
    reverse_number[9] = "NIN"



    for i in range(N) :
        backup[i] = number[org[i]]
    backup.sort()

    # print(number[0])
    for i in range(N) :
        result[i] = reverse_number[backup[i]]

    print(f'#{testcase}')
    print(f'{" ".join(result)}')


    # for i in range(N) :
    #     result[i] = number[backup[i]]






    # print(org)
    # print(number)

    # ///////////////////////////////////////////////////////////////////////////////////
