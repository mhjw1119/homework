import sys
sys.stdin = open('input.txt', 'r')
import heapq
import math


'''
첫 정 점에서 시작한다. 
해당 정점을 들렸다는 표시를 한다.
그 정점 말고 다른 정점들을 다 확인하면서 거리값을 계산하여 힙에다 다 넣는다.
그 거리값들중에 가장 작은 값과 인덱스를 다시 힙에 넣는다.
반복한다
'''

T = int(input())
def distance (xx,yy) :
    result = xx ** 2 + yy ** 2
    return result

def MST (tax) :
    pq = [(0,0)]
    visit = [0] * N
    min_cost = 0

    while pq :
        cost, node = heapq.heappop(pq)

        if visit[node]:
            continue

        visit[node] = 1
        min_cost += cost

        for next_node in range(N) :
            if visit[next_node] :
                continue
            next_cost = distance(abs(x[node]-x[next_node]),abs(y[node]-y[next_node])) * E
            heapq.heappush(pq,(next_cost, next_node))
    return round(min_cost)




for tc in range( 1, T + 1 ) :
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    print(f'#{tc} {MST(E)}')