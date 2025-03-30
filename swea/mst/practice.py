import heapq

def prim(start_node) :
    pq = [(0,start_node)]
    visit = [0] * V
    min_weight = 0

    while pq :
        weight, node = heapq.heappop(pq)

        if MST[node] :
            continue
        MST[node] = 1
        min_weight += weight

        for next_node in range(V):
            if graph[node][next_node] == 0
                continue

            if MST[next_node] :
                continue
            heapq.heappush(pq,(graph[node][next_node], next_node))

    return min_weight

V,E = map(int, input())