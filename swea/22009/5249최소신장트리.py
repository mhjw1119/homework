import sys
sys.stdin = open('input.txt', 'r')

import heapq

def MST ( start_node):
    pq = [(0, start_node)]
    check = [0] * (V+1)
    min_sum = 0
    cnt = 0

    while pq :
        weight, node = heapq.heappop(pq)

        if check[node] :
            continue
        #
        if cnt == V+1 :
            break
        check[node] = 1
        cnt += 1
        min_sum += weight



        for next_node, next_weight in graph[node] :
            if check[next_node]:
                continue

            heapq.heappush(pq,(next_weight, next_node))

    return min_sum




T = int(input())

for tc in range( 1, T + 1 ) :
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        graph[arr[i][0]] .append((arr[i][1], arr[i][2]))
        graph[arr[i][1]].append((arr[i][0], arr[i][2]))
    print(f'#{tc} {MST(0)}')


