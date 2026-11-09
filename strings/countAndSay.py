def countAndSay(n):
    curr = "1"
    for i in range(2, n + 1):
        count = 1
        rle = ""
        for j in range(1, len(curr) + 1):
            if j < len(curr) and curr[j] == curr[j - 1]:
                count += 1
            else:
                rle += str(count) + curr[j - 1]
                count = 1
        curr = rle
    return curr

print(countAndSay(4))   

"""
    output
    1 - n  = 1
    11 - n = 2
    21 - n = 3
    1211 - final answer for n = 4
"""