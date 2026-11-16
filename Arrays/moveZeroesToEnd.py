def moveZeroesToEnd(arr):
    x = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[x]
            arr[x] = arr[i]
            arr[i] = temp
            x += 1
    return arr

print(moveZeroesToEnd([0,1,0,3,12]))