def decodeString(s):
    i = 0
    def decode():
        nonlocal i
        res = ""
        num = 0
        while(i < len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
                i += 1
            elif char == "[":
                i += 1
                str = decode();
                res = res + str * num
                num = 0
            elif char == "]":
                i += 1
                return res
            else:
                res += char
                i += 1

        return res
    return decode()    

print(decodeString("3[a2[b]c]"))
