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
def distance (x,y) :
    return math.sqrt(x ** 2 + y ** 2)


def di():
    back = [0,0,None]
    check = set()

    while back :
        weight, now_node, pre_node = heapq.heappop(back)

        if pre_node is not None :                   # 첫 번째 순회인지 확인
            check.add(pre_node)
            now_x, now_y = idx_dict[now_node]
            most_short_distance = int('inf')
            most_short_idx = None
            for next_key in range(N) :          # 정점들중에 가장 가까운 거리값의 키값 찾기
                if next_key == now_node or next_key == pre_node :       # 자기 자신과 바로 직전에 노드면은 안됨
                    continue
                pre_x, pre_y = idx_dict[next_key]
                now_distance = distance(abs(now_x-pre_x),abs(now_y-pre_y))

                if most_short_distance > now_distance :     # 가장 짧은 거리 찾으면 거리랑 인덱스값 저장
                    most_short_distance = now_distance
                    most_short_idx = next_key
        heapq.heappush(back,(weight+most_short_distance, next_key, now_node))


for tc in range( 1, T + 1 ) :
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    idx_dict = {}
    for i in range(N):
        idx_dict[i] = [x[i],y[i]]
    real_result = 1000000000000000000000000000000000000000000000000000000000
    # print(idx_dict)
    # print(f'#{tc} {real_result}')