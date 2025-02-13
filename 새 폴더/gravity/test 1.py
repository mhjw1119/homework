# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
# 최대값의 인덱스 값이 맨 오른쪽이면  오른쪽부터 순회해서 n-1이 n보다 클 때
# 만약 정렬 전 가장 최대 값이
# 아 그냥 순회 돌면서 해당 인덱스의 값보다 n+1 큰 인덱스 값이 자기 자신보다 크면 되는구나?
# 맨 왼쪽부터 순회를 도는데, 자기보다 오른쪽에 작은 값들이 몇 번이나 나오는 지 카운트 한다. 그리고 카운트 하면서 총 갯수에서
# 해당 갯수를 빼다가 0이 되면 전체 길이에서 해당 인덱스 값을 빼줘서 카운트에 더한다

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    box = list(map(int,input().split()))
    box_max_list = [0] * N

    for i in range(N) :
        count = 0
        if i == N-1 :
            break
        else :

            for x in range(i,N) :
                if box[i] > box[x] :
                    count += 1

        box_max_list[i] = count
    print(box_max_list)


    result = max(box_max_list)

    print(f'#{test_case} {result}')
