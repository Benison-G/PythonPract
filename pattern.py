def pattern():
    for i in range(5):
        row = "";
        for _ in range(5 - i):
            row += " "
        for _ in range(2 * i - 1):
            row += "*"
        print(row);

pattern()
