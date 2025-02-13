
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    number = list(map(int,input()))
    max = 0
    index = 0
    print(number)

    print(number.count(9))
    for i in range(N) :
        print(number.count(number[i]))

        if number.count(number[i]) > max :
            max = number.count(number[i])
            index = i
        elif number.count(number[i]) == max :
            if number[i] > number[index] :
                index = i
    print(f'#{test_case} {number[index]} {max}')
    # ///////////////////////////////////////////////////////////////////////////////////
