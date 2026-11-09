def reverseVowels(str):
    s = [*str]
    vowels = set(["a","e", "i", "o", "u"]) 

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left]  in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
    
    return "".join(s)

print(reverseVowels("hello"))
    