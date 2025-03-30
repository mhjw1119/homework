import sys
sys.stdin = open('input.txt', 'r')

import heapq

def MST () :
    min_w = 0
    pq = [(0,0)]
    check = [0] * (V + 1)
    cnt = 0

    while pq :
        weigh,node  = heapq.heappop(pq)

        if check[node] :
            continue


        check[node] = 1
        cnt += 1
        min_w += weigh

        if cnt == V + 1 :
            break

        for next_weigh, next_node in graph[node] :

            heapq.heappush(pq, (next_weigh,next_node))

    return min_w



T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E) :
        s,e,w = map(int, input().split())
        graph[s].append( [w,e] )
        graph[e].append([w, s])

    print(f'#{tc} {MST()}')
