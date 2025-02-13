
'''
가운데를 기준으로 양쪽을 바꾸고 바꿀 때 추가적으로 해당 글자를 거울에 비친 글자로 바꾼다
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    case = list(input())
    N = len(case)

    def change ( char ) :
        if char == 'b' :
            return 'd'
        elif char == 'd' :
            return 'b'
        elif char == 'p' :
            return 'q'
        elif char == 'q' :
            return 'p'

    for i in range(N//2) :
        case[i] = change(case[i])
        case[N-1-i] = change(case[N-1-i])
        case[i], case[N-1-i] = case[N-1-i], case[i]

    if N%2 != 0 :
        case[N//2] = change(case[N//2])

    print(f'#{test_case} {"".join(case)}')
    # ///////////////////////////////////////////////////////////////////////////////////
