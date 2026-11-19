def overlappingIntervalsCount(intervals):
    count = 0;
    lastEnd = float('-inf')

    intervals.sort(key=lambda x: x[1])
    for [start, end] in intervals:
        if start < lastEnd:
            count += 1
        else: 
            lastEnd = end
    return count

print(overlappingIntervalsCount([[1,2],[2,3],[3,4],[1,3]])) # prints 1
print(overlappingIntervalsCount([[1,2],[1,2],[1,2]])) # prints 2