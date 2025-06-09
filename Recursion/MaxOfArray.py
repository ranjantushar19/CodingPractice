def maxOfArray(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    max_arr_n_minus_1 = maxOfArray(arr, idx+1)
    if arr[idx] >= max_arr_n_minus_1:
        return arr[idx]
    else:
        return max_arr_n_minus_1

a = [23, 37, 13, 93, 67, 11, 49]
print(maxOfArray(a,0))