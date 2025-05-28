def minimumPlatformsRequired(srt_arr, end_arr):
    n = len(srt_arr)
    res = []

    for i in range(n):
        res.append([srt_arr[i], 1])
        res.append([end_arr[i], -1])

    res.sort()

    min_plat_req = 0
    curr_plat_req = 0
    for i in range(2*n):
        curr_plat_req += res[i][1]
        min_plat_req = max(curr_plat_req, min_plat_req)
        '''
        Here max will give the min no. of required platforms.
        '''

    return min_plat_req


start_time = [900, 945, 955, 1100, 1500, 1800]
end_time = [920, 1200, 1130, 1150, 1900, 2000]

print(minimumPlatformsRequired(start_time, end_time))



