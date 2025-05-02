def climbingStairsRecursion(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    n_minus_1 = climbingStairsRecursion(n - 1)
    n_minus_2 = climbingStairsRecursion(n - 2)
    n_minus_3 = climbingStairsRecursion(n - 3)

    return n_minus_1 + n_minus_2 + n_minus_3

def climbingStairsDP(n):
    if n < 3:
        return n
    arr = [0] * (n + 1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    return arr[n]





print(climbingStairsRecursion(4))
print(climbingStairsDP(4))