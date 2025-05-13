def jumpGameGreedy(arr):
    n = len(arr)
    max_reachable = 0

    if arr[0] == 0:
        return False
    if all(arr):
        return True

    for i in range(n):
        if max_reachable < i:
            return False
        max_reachable = max(i + arr[i], max_reachable)
        #print(f"i : {i}, max reachable : {max_reachable}")
    return True


def jumpGameRecursion(arr, idx):
    if idx == len(arr) - 1:
        return True
    if arr[idx] == 0:
        return False

    max_res = False
    for i in range(arr[idx]):
        res = jumpGameRecursion(arr, idx + i + 1)
        max_res = max(res, max_res)

    return max_res


def jumpGameDP(arr):
    if arr[0] == 0:
        return False
    if all(arr):
        return True

    n = len(arr)
    res = [False] * n
    res[0] = True

    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if j + arr[j] >= i:
                res[i] = True
                break
    return res[n-1]




a = [1, 3, 2, 0, 2]
print(jumpGameGreedy(a))
print(jumpGameRecursion(a, 0))
print(jumpGameDP(a))
#b = [1, 2, 1, 0, 2]
#print(jumpGameGreedy(b))
#print(jumpGameRecursion(b, 0))
#print(jumpGameDP(b))
