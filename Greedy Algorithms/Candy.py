def candy(arr):
    n = len(arr)

    res = [1] * n

    for i in range(1,n):
        if arr[i] > arr[i-1]:
            res[i] = res[i-1] + 1

    for j in range(n-2, -1, -1):
        if arr[j] > arr[j+1]:
            res[j] = res[j+1] + 1

    return sum(res)

a = [1, 2, 2]
print(candy(a))
b = [5, 4, 3, 2]
print(candy(b))