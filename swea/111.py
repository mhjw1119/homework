numbers = [1,1,1,1,1]
target = 3

check1 = [0] * len(numbers)


def dfs(depth, check):
    result = 0
    answer = 0
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
    dfs(depth + 1, check)

    check[depth] = 1
    dfs(depth + 1, check)


print(dfs(0, check1))
print(answer)