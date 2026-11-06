def validParenthesis(str):
    openCount = closeCount = 0;

    for i in range(len(str)):
        if str[i] == "(":
            openCount += 1
        else:
            if openCount == 0:
                closeCount += 1
            else:
                openCount -= 1

    return f"{openCount + closeCount} parenthesis to be added"

print(validParenthesis("(())))")) #2 parenthesis to be added 
        