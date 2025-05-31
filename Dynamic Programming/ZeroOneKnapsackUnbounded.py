def zeroOneKnapsackUnbounded(arr, bag_weight):
    n = len(arr)
    res = [0] * (bag_weight + 1)

    for i in arr:
        for j in range(1, bag_weight + 1):
            if i[1] <= j:
                res[j] = max(res[j - i[1]] + i[0], res[j])

    return res[-1]

price_weight_map = [[15, 2], [14, 5], [10, 1], [45, 3], [30, 4]]
max_bag_weight = 7

print(zeroOneKnapsackUnbounded(price_weight_map, max_bag_weight))