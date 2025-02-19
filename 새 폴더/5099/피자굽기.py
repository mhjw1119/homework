# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    que = [0] * (N )
    count = 0
    flag = 0
    d_count = 0
    for i in range(N) :
        que[i] = [arr[i],i]

    while flag != 1 :
        for i in range(N) :
            if len(que) == 1 :
                break
            if que[i][0] == 0 :
                nque = N+count
                if nque < M :
                    que[i] = [arr[nque],nque]
                    # que[i].append(nque)
                    count += 1
                else :
                    que.pop(i)
                    if len(que) == 1 :
                        flag = 1
                        break
                    # for k in range(N) :
                    #     if que[k][0] != 0 :
                    #         d_count += 1
                    # if d_count == 1:
                    #     flag = 1
                    #     break
            else:
                # for k in range(N):
                #     if que[k][0] != 0:
                #         d_count += 1
                # if d_count == 1:
                #     flag = 1
                #     break
                que[i][0] = que[i][0]//2

    # for i in range(N) :
    #     if 0 not in que[i]  :
    #         result = que[i][-1]
    print ( que[0][-1]+1 )
