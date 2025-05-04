def minimumCostPath(arr):
    r = len(arr)
    c = len(arr[0])
    #res = [[0] * c] * r
    res = [[0 for _ in range(c)] for _ in range(r)]
    res[r - 1][c - 1] = arr[r - 1][c - 1]

    for j in range(c - 2, -1, -1):
        res[r -1][j] = arr[r -1][j] + res[r -1][j + 1]

    for i in range(r - 2, -1, -1):
        res[i][c-1] = arr[i][c-1] + res[i+1][c-1]

    # for i in res:
    #     print(i)

    for i in range(r-2, -1, -1):
        for j in range(c-2, -1, -1):
                res[i][j] = arr[i][j] + min(res[i + 1][j], res[i][j + 1])

    for i in res:
        print(i)
    return res[0][0]

cost = [[2, 8, 4, 1, 6, 4, 2],
        [6, 0, 9, 5, 3, 8, 5],
        [1, 4, 3, 4, 0, 6, 5],
        [6, 4, 7, 2, 4, 6, 1],
        [1, 0, 3, 7, 1, 2, 7],
        [1, 5, 3, 2, 3, 0, 9],
        [2, 2, 5, 1, 9, 8, 2]]

print(minimumCostPath(cost))