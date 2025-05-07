def CoinChangeCombination(arr, target):
    n = len(arr)
    res = [0] * (target + 1)

    res[0] = 1
    for i in arr:
        for j in range(i, target +1):
            res[j] += res[j - i]
        #print(f"{res = }")
    return res[target]

denominations = [2, 3, 5, 6]
target_sum = 10

print(CoinChangeCombination(denominations, target_sum))