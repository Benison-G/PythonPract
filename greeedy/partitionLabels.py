# Divide the string into partition such that, no character occurs
# in more than 1 partition and return the length of each partition 
# in an array

def partitionLabels(s):
    ans = []
    last = {}

    for i in range(len(s)):
        last[s[i]] = i

    start = end = 0

    for i in range (len(s)):
        end = max(end, last[s[i]])
        if (i == end):
            ans.append(end - start + 1)
            start = end + 1
    return ans

s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))