def countAndSay(n):
    curr = "1"
    for i in range(2, n + 1):
        count = 1
        rle = ""
        for j in range(1, len(curr)):
            if curr[j] == curr[j - 1]:
                count += 1
            else:
                rle += str(count) + curr[j - 1]
                count = 1
        rle += str(count) + curr[-1]
        curr = rle
    return curr

print(countAndSay(4))            