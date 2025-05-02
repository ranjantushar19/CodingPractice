def climbingStairsMinimumJumps(arr):
    n = len(arr)
    res = [n] * (n + 1)
    res[n] = 0

    for i in range(n-1, -1, -1):
        if arr[i] != 0:
            for j in range(1, arr[i] + 1):
                if i + j <= n:
                    res[i] = min(1 + res[i + j], res[i])
                else:
                    break
        print(f"{res =}")
    return res[0]


max_jump = [3, 2, 4, 2, 0, 2, 3, 1, 2, 2]
print(climbingStairsMinimumJumps(max_jump))