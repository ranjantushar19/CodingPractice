def targetSumSubset(arr, target):
    n = len(arr)
    res  = [[False for _ in range(target + 1)] for _ in range(n+1)]

    for i in range(n+1):
        res[i][0] = True
    for j in range(1, target + 1):
        if j == arr[0]:
            res[1][j] = True

    for i in range(2, n + 1):
        for j in range(1, target + 1):
            res[i][j] = max(res[i-1][j], res[i-1][j - arr[i - 1]])

    # for i in range(n + 1):
    #     print(res[i])

    return res[-1][-1]

denomination = [4, 2, 7, 1, 3]
target_sum = 10

print(targetSumSubset(denomination, target_sum))