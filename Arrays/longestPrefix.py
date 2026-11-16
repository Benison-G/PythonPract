def longestPrefix(strs):
    x = 0
    while (x < len(strs[0])):
        ch = strs[0][x]

        for i in range(1, len(strs)):
            if ch != strs[i][x] or x == len(strs[i]):
                return strs[0][0: x]
        x += 1
    return strs[0]

print(longestPrefix(["flower", "flow", "flight"]))