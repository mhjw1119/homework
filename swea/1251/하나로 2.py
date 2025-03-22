import sys
import heapq

sys.stdin = open('input.txt', 'r')


def dijkstra():
    backup = [(0, 0, 0)]
    while backup :
        weight, y, x = heapq.heappop(backup)   # bfs 큐 활용하는 것 과 똑같다. 힙 배열에 맨 앞에 있는 배열의 값을 pop하여 확인한다.
        if y == N-1 and x == N -1 :
            return weight   # 종착지인 맨오른쪽 맨 아래에 도착하면 탐색을 종료하고 가중치 값을 반환한다.

        weight += arr[y][x]     # 종착지가 아닌 경우 가중치를 더해놓는다.

        if weight < check[y][x] :   # 만약 해당 인덱스의 가중치 값보다 현재 가중치 값이 작다면 인덱스의 가중치 값을 최소로 갱신한다.
            check[y][x] = weight
        else :
            continue    # 만약 해당 인덱스의 가중치 값보다 크면 컨티뉴로 해당 반복은 넘겨버린다. 이걸 해줘야 같은 곳에 반복되지 않고 새로운 곳으로 갈 수 있어 무한 루프를 막는다

        for dy, dx in [0,1],[1,0],[0,-1],[-1,0]: # 이건 걍 델타 탐색
            ny = dy + y
            nx = dx + x
            if -1 < ny < N and -1 < nx < N :
                if nx == 0 and ny == 0 :     # 이건 출발점으로 되돌아 오지 못하게 막는 코드다. 출발점은 항상 가중치가 0이어서 되돌아가지 못하게 막아야한다.
                    continue
                heapq.heappush( backup, (weight, ny, nx) )  # 다음으로 위치할 곳을 찾았으면 현재의 가중치와 다음 이동할 인덱스값을 함께 힙에 푸시한다.
T = int(input())

for tc in range( 1, T + 1 ) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    check = [[1000000000000000000000000000000000000000000000000000000000] * (N) for _ in range(N)]
    # 다익스트라를 구현하려면 복사본만들고 각 인덱스를 무한대로 초기해야한다
    print(f'#{tc} {dijkstra()}')