# for the given input no two adjacent characters should be duplicate

def reorganize(s):
    freq = {}
    maxFreq = 0

    for char in s:
        freq[char] = freq.get(char, 0) + 1
        maxFreq = max(maxFreq, freq[char])

    n = len(s)
    if maxFreq > (n + 1 // 2):
        return ""

    chars = sorted(freq, key=lambda ch: freq[ch], reverse=True)
    res = [None] * n
    i = 0
    for ch in chars:
        count = freq[ch]
        while count > 0:
            if i >= n:
                i = 1
            res[i] = ch
            count -= 1
            i += 2
    return "".join(res)


print(reorganize("aab"))
