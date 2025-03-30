import sys
sys.stdin = open('input.txt', 'r')

import heapq

def di () :
    pq = [(0,0)]
    check = [1000000000000000] * (V + 1)
    check[0] = 0
    while pq :
        weigh, node = heapq.heappop(pq)


        if check[node] < weigh :
            continue

        for next_weigh, next_node in graph[node] :
            now_weigh = weigh + next_weigh
            if check[next_node] > now_weigh :
                check[next_node] = now_weigh
                heapq.heappush(pq, (now_weigh,next_node))

    return check[V]




T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E) :
        s,e,w = map(int, input().split())
        graph[s].append( [w,e] )

    print(f'#{tc} {di()}')
