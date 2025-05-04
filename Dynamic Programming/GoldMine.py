def goldMine(arr):
    r = len(arr)
    c = len(arr[0])
    res = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        res[i][c-1] = arr[i][c-1]

    for j in range(c - 2, -1, -1):
        for i in range(r):
            if i == 0:
                res[i][j] = arr[i][j] + max(res[i][j+1], res[i+1][j+1])
            elif i == r - 1:
                res[i][j] = arr[i][j] + max(res[i][j + 1], res[i - 1][j + 1])
            else:
                res[i][j] = arr[i][j] + max(res[i - 1][j + 1], res[i][j + 1], res[i + 1][j + 1])

    max_gold = 0
    for i in range(r):
        max_gold = max(max_gold, res[i][0])

    for i in res:
        print(i)

    return max_gold

gold_field = [[0, 1, 4, 2, 8, 2],
              [4, 3, 6, 5, 0, 4],
              [1, 2, 4, 1, 4, 6],
              [2, 0, 7, 3, 2, 2],
              [3, 1, 5, 9, 2, 4],
              [2, 7, 0, 8, 5, 1]]

print(goldMine(gold_field))

