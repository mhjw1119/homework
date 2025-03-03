T = int(input())


for testcase in range(1,T+1) :

    arr = list(input())
    stack = []
    num = []
    rt = ['-','+']
    ry = ['*','/']
    for i in range(len(arr)):
        if arr[i]=='+' or arr[i]== '-' or arr[i]=='*' or arr[i]=='/' :
            stack.append(arr[i])
        else:
            num.append(arr[i])
