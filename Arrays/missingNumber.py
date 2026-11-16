def missingNumber(arr):
    n = len(arr);
    totalSum = n * (n + 1) // 2
    partialSum = 0

    for i in range(len(arr)):
        partialSum += arr[i]

    return totalSum - partialSum

print(missingNumber([4,0,2,5,1]))
print(missingNumber([0, 1]))