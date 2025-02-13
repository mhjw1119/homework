
# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제

#  조망권 조건 : 해당 인덱스 양옆에 두칸까지 비어 있으면 된다.
#   반대로 생각하면 해당 인덱스에 양옆이 해당 인덱스보다 크면 조망권을 얻을 가능성이 없다.
#   건물의 높이가 저장되어 있는 리스트를 순회 한다.
#   만약 왼쪽으로 한칸 가서 그 인덱스의 값이 기준 인덱스 값보다 작으면 왼쪽 두칸으로 가서 거기도 기준 인덱스의 값보다 작으면
#   오른쪽도 똑같이 한다. 이 때 왼쪽 오른쪽 칸들의 가장 최고 값을 확인한다.
#   양쪽 조망권이 확보 됐다면 기준 인덱스 값에서 양쪽 가장 최고값을 빼주면 조망권이다.



import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    high = list(map(int, input().split()))
    result = 0
    for i in range(2,len(high)-2) :
        high_max = 0
        if high[i] >= high[i-1] and high[i+1] <= high[i] and high[i] >= high[i-2] and high[i+2] <= high[i]:
                print(high[i])
                for x in range(i-2,i+3) :
                    if x == i :
                        print(f'x==i : {i}')
                        continue
                    print(f'x : {x}')
                    if high_max < high[x] :
                        high_max = high[x]
        else :
            continue
        print(f'high_max : {high_max}')
        print(f'high : {high[i]}')

        result += high[i]-high_max
        print('-----------')
        print(result)
        print('-----------')

    print(f'#{test_case} {result}')
                


