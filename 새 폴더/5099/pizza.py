import sys
sys.stdin = open("input.txt", "r")
from collections import  deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    count = N
    fire = [0]  * (N+1)


    print(fire)

    print(fire.deque())

