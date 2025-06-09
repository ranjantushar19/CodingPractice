def DisplayArrayReverse(arr,idx):
    if idx == len(arr):
        return
    DisplayArrayReverse(arr, idx+1)
    print(arr[idx])

a = [10, 20, 30, 40, 50, 60, 70]
DisplayArrayReverse(a, 0)
