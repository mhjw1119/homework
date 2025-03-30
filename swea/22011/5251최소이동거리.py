import sys
sys.stdin = open('input.txt', 'r')

import heapq

def di ():
    check = [10000000000000000000000000000000000000000] * (V+1)
    heap = []
    check[0] = 0
    heapq.heappush(heap,(0,0))
    while heap :
        weight, node = heapq.heappop(heap)

        if check[node] < weight :
            continue

        for next_node, next_weight in graph[node] :
            cost = weight + next_weight
            if cost < check[next_node] :
                check[next_node] = cost
                heapq.heappush(heap,(cost, next_node))

    return check[V]




T = int(input())

for tc in range( 1, T + 1 ) :
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        graph[arr[i][0]] .append((arr[i][1], arr[i][2]))
        # graph[arr[i][1]].append((arr[i][0], arr[i][2]))
    print(f'#{tc} {di()}')


