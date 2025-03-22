import sys
sys.stdin = open('input.txt', 'r')
import heapq
import math

T = int(input())

def di():
    backup = [(0,0,0)]
    cnt = 0
    while backup :
        weight, heap_x, heap_y = heapq.heappop(backup)
        check[cnt] = 1
        cnt += 1


        for ii in range(N) :
            if check[ii] == 1 :
                continue
            nx = idx[ii][0]
            ny = idx[ii][1]
            if nx == heap_x or ny == heap_y :
                weight += E * ((abs(heap_x - nx) + abs(heap_y - ny)) ** 2)
            else:
                weight += E * math.sqrt((abs(heap_x - nx) + abs(heap_y - ny)))

            heapq.heappush(backup, (weight, idx[ii][0], idx[ii][1]))
    return weight

for tc in range( 1, T + 1 ) :
    N = int(input())
    idx = [[] for _ in range(N)]
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for i in range(N):
        idx[i].append(x[i])
        idx[i].append(y[i])
    check = [0] * N
    E = float(input())
    print(di())