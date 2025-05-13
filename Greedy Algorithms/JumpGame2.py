def jumpGame2Greedy(arr):
    n = len(arr)

    min_jumps = 0
    min_boundary = 0
    max_boundary = 0
    while max_boundary < (n-1):
        farthest = 0
        for i in range(min_boundary, max_boundary + 1):
            farthest = max(farthest, i + arr[i])
        min_boundary =  max_boundary + 1
        max_boundary = farthest
        min_jumps += 1

    return min_jumps


def jumpGame2Recursion(arr, idx, jumps):
    if idx >= len(arr) - 1:
        return jumps
    min_jumps = len(arr) + 100
    for i in range(arr[idx]):
        res = jumpGame2Recursion(arr, idx + i + 1, jumps + 1)
        min_jumps = min(res, min_jumps)

    return min_jumps


def jumpGame2DP(arr):
    n = len(arr)
    res = [n] * n
    res[0] = 0

    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if j + arr[j] >= i:
                res[i] = min(res[j]+1, res[i])
    return res[n-1]




a = [1, 3, 2, 0, 2]
print(jumpGame2Greedy(a))
print(jumpGame2Recursion(a, 0, 0))
print(jumpGame2DP(a))
b = [2, 3, 1, 4, 1, 1, 1, 2]
print(jumpGame2Greedy(b))
print(jumpGame2Recursion(b, 0, 0))
print(jumpGame2DP(b))
