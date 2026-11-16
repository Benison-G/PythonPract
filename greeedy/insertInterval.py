def insertInterval(intervals, newinterval):
    n = len(intervals)
    res = []

    i = 0

    while i < n and intervals[i][1] < newinterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newinterval[1]:
        newinterval[0] = min(newinterval[0], intervals[i][0])
        newinterval[1] = max(newinterval[1], intervals[i][1])
        i += 1

    res.append(newinterval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res

print(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
