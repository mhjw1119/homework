import sys
sys.stdin = open("input.txt", "r")

#왼쪽 오른쪽 나누어서 받는다.
'''
스타트에서 시작해서 인접한 접점 중 탐색하지 않은 곳을 간다
이 때 접점을 푸시한다
만약 더이상 갈 수 있는 접점이 없으면 스택을 팝해서 바로 전의 접점으로 간다
거기서 탐색하지 않은 접점을 찾아서 가고, 그것 마저도 없으면 탐색을 종료하고 실패를 뱉는다


'''


def dfs (start, end) :
    stack = []
    visit = [0] * 100
    top = -1
    while 1 :
        if left[start] == end or right[start] == end :
            return 1

        if visit[start] == 0 :
            visit[start] = 1
            stack.append(start)

        if visit[left[start]] == 0 :
            start = left[start]

        else:
            if visit[right[start]] == 0 :
                start = right[start]
            else:
                if len(stack) == 0 :
                    return 0
                start = stack.pop()






T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T +1):
    tc, N = map(int,input().split())
    arr = list(map(int,input().split()))
    left = [0] * 100
    right = [0] * 100
    for i in range(0,len(arr),2):
        if left[arr[i]] == 0 :
            left[arr[i]] = arr[i+1]
        else:
            right[arr[i]] = arr[i + 1]
    print(f'#{test_case} {dfs(0,99)}')

