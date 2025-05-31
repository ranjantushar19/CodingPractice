def zeroOneKnapsack(arr, bag_weight):
    n = len(arr)
    res = [[0 for _ in range(bag_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, bag_weight + 1):
            if arr[i-1][1] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i - 1][j-arr[i-1][1]] + arr[i-1][0], res[i - 1][j])
    return res[-1][-1]


price_weight_map = [[15, 2], [14, 5], [10, 1], [45, 3], [30, 4]]
max_bag_weight = 7

print(zeroOneKnapsack(price_weight_map, max_bag_weight))