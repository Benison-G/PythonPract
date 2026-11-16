def palindrome(arr1, arr2):
    n = len(arr1) - 1;
    for i in range(len(arr1)):
        if (arr1[i] != arr2[n - i]):
            return False
    return True

print(palindrome([1,2,3,4,5], [5,4,3,2,1]))
    