def displayArray(arr,idx):
    if idx == len(arr):
        return
    print(arr[idx])
    displayArray(arr, idx+1)

a = [10, 20, 30, 40, 50, 60, 70]
displayArray(a, 0)
