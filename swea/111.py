numbers = [1,1,1,1,1]
target = 3

check1 = [0] * len(numbers)
answer = 0
def dfs(depth, check, answer):
    result = 0
    if depth == len(numbers):
        for i in range(len(numbers)):
            if check[i] == 0:
                result -= numbers[i]
            else:
                result += numbers[i]
        if result == target:
            answer += 1
        return

    check[depth] = 0
    dfs(depth + 1, check, answer)

    check[depth] = 1
    dfs(depth + 1, check, answer)

real_result = 0
dfs(0,check1,0)
print(answer)
#
# def dfs(depth, check):
#     global answer
#     result = 0
#     if depth == len(numbers):
#         for i in range(len(numbers)):
#             if check[i] == 0:
#                 result -= numbers[i]
#             else:
#                 result += numbers[i]
#         if result == target:
#             answer += 1
#         return answer
#
#     check[depth] = 0
#     dfs(depth + 1, check)
#
#     check[depth] = 1
#     dfs(depth + 1, check)
#     return answer
# real_result = 0
# dfs(0,check1)
# print(answer)
