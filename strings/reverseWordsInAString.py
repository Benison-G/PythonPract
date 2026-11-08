def reverseWords(text):
    splits = splitWords(text)
    for i in range(len(splits) // 2):
       last = len(splits) - i - 1;
       temp = splits[i];
       splits[i] = splits[last]
       splits[last] = temp
    
    return " ".join(splits)

def splitWords(text):
    words = []
    word = ""

    for char in text:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else: 
            word += char

    if word:
        words.append(word)

    return words

print(reverseWords(" blue  is   sky   the"))