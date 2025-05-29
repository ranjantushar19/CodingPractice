def shortestJoFirstAvgWaitTime(arr):
    n = len(arr)
    arr.sort()

    totalWaitTime = 0
    completeTime = 0
    for i in range(n):
        totalWaitTime = completeTime + arr[i]
        completeTime = totalWaitTime

    return totalWaitTime/n


a = [4, 3, 7, 1, 2]
print(shortestJoFirstAvgWaitTime(a))

