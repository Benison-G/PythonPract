def mergeIntervals(intrls):
    
    intervals = sorted(intrls, key=lambda x: x[0])

    result = [intervals[0]]

    for i in range(1, len(intervals)):
        if (intervals[i][0] <= result[len(result) - 1][1]):
            result[len(result) - 1][1] = max(result[len(result) - 1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    return result


print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))