def coinChangePermutation(arr, target):
    n = len(arr)
    res = [0] * (target + 1)
    res[0] = 1

    for j in range(1, target + 1):
        for i in arr:
            if j - i >= 0:
                res[j] += res[j-i]
    return res[target]



denominations = [2, 3, 5, 6]
target_sum = 10

print(coinChangePermutation(denominations, target_sum))

