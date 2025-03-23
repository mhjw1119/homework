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

def di(first_x, first_y):
    result = [100000000000000000000000000000000000000000] * N

    backup = [(0,0,first_x,first_y,None)]
    cnt = 0
    while backup :
        weight, heap_idx, heap_x, heap_y, prev_node = heapq.heappop(backup)
        # check[heap_idx] = 1


        if weight < result[heap_idx] :
            result[heap_idx] = weight
        else:
            continue
        if prev_node is not None :
            check.add(prev_node)



        for ii in range(N) :
            back = 0

            # if ny == heap_y and nx == heap_x :
            #     continue
            nx = idx[ii][0]
            ny = idx[ii][1]
            if ii in check :
                continue

            # if ny == heap_y and nx == heap_x :
            #     continue
            if nx == heap_x or ny == heap_y :
                back = weight + (E * ((abs(heap_x - nx) + abs(heap_y - ny)) ** 2))
            else:
                length = math.sqrt(abs(heap_x - nx)**2 + abs(heap_y - ny)**2)
                back = weight+ (E * (length ** 2))

            heapq.heappush(backup, (back ,ii, idx[ii][0], idx[ii][1], heap_idx))
    return result[-1]

for tc in range( 1, T + 1 ) :
    N = int(input())
    idx = [[] for _ in range(N)]
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for i in range(N):
        idx[i].append(x[i])
        idx[i].append(y[i])

    E = float(input())
    real_result = 1000000000000000000000000000000000000000000000000000000000
    for f_x, f_y in idx :
        # check = [0] * N
        check = set()
        real_result = min(real_result,int(di(f_x,f_y)))
    print(f'#{tc} {real_result}')