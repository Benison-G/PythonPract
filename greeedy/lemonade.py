def lemonade(bills): 
    wallet = [0, 0]

    for i in range(len(bills)):
        if bills[i] == 5:
            wallet[0] += 1
        elif bills[i] == 10:
            wallet[1] += 1
            wallet[0] -= 1
        else:
            if wallet[1]:
                wallet[1] -= 1
                wallet[0] -= 1
            else:
                wallet[0] = wallet[0] - 3
        if wallet[0] < 0:
            return False
    return True

print(lemonade([5,5,5,10,20]))
print(lemonade([5,5,10,10,20]))