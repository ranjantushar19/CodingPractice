def insertInterval(arr, new_intv):
    n = len(arr)
    res = []

    i = 0
    while i < n and arr[i][1] < new_intv[0]:
        '''
        While the end times of intervals in array is less than start time of new interval.
        I.e. intervals strictly lower/before the new interval to be added.
        '''
        res.append(arr[i])
        i += 1
    while i < n and arr[i][0] <= new_intv[1]:
        '''
        While the start time of new interval is less than start times of intervals in array.
        I.e. until the intervals in the array are not strictly greater than new interval (including the overlapping portion).
        '''
        new_intv[0] = min(arr[i][0], new_intv[0])
        new_intv[1] = max(arr[i][1], new_intv[1])
        i += 1
    res.append(new_intv)

    while i < n:
        '''
        Append the remaining intervals.
        '''
        res.append(arr[i])
        i += 1

    return res


existing = [[1, 5], [7, 9], [10, 13], [16, 19], [20, 25]]
new = [12, 20]

c = insertInterval(existing, new)
print(f"{c = }")