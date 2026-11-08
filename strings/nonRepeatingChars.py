def nonRepeatingCharacters(s):
    map = {}

    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1

    res = ""

    for char, count in map.items():
        if count == 1:
            res += char

    return res

print(nonRepeatingCharacters("swiss"))
