def nMeetingsOneRoom(srt, end):
    n = len(srt)
    start_sorted = sorted(zip(srt,end), key=lambda x : x[1])
    print(f"{start_sorted = }")
    max_meetings = 1
    prev_meeting = start_sorted[0]

    for i in range(1, n):
        if start_sorted[i][0] >= prev_meeting[1]:
            max_meetings += 1
            prev_meeting = start_sorted[i]

    return max_meetings

start_time = [0, 3, 1, 5, 5, 8]
end_time = [5,  4, 2, 9, 7, 9]
print(nMeetingsOneRoom(start_time, end_time))