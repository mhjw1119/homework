'''
두 수 가 같지 않으면 체크 진행
그 두 수의 인덱스 범위 내에 다른 수가 있다면
카운트 증가

'''

T = int(input())

for tc in range(1,T+1 ) :
    N = int(input())
    arr = list(map(int,input().split()))

