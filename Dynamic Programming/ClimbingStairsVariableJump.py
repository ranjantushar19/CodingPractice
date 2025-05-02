def climbingStairsVariableJump(arr):
    n = len(arr)
    res = [0] * (n + 1)
    res[n] = 1

    for i in range(n-1, -1, -1):
        if arr[i] != 0:
            #print(f"{i = }, {arr[i] = }")
            for j in range(1, arr[i] + 1):
                if i + j <= n:
                    #print(f"{i+j = }")
                    res[i] += res[i + j]
            #print(f"{res = }")
    return res[0]



step = [3, 3, 0, 2, 2, 3]
print(climbingStairsVariableJump(step))