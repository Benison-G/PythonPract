def leastIntervals (tasks, n):
    maxFreq = 0
    map = {}
    charCountWithMaxFreq = 0

    for i in range(len(tasks)):
        map[tasks[i]] = map.get(tasks[i], 0) + 1
        freq =map[tasks[i]]
        if (freq > maxFreq):
            maxFreq = freq
            charCountWithMaxFreq = 1
        elif freq == maxFreq:
            charCountWithMaxFreq += 1

    cycles = (n + 1) * (maxFreq - 1) + charCountWithMaxFreq

    return max(len(tasks), cycles)

arr = ["A","A","A","B","B","B"];

print(leastIntervals(arr, 2))

