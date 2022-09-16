# Given an array of size n we have to find the smallest positive integer which is not present in the array.


def firstMissingPositive(arr):
    n = len(arr)
    # Loop to traverse the whole array
    for i in range(n):
       
        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
     
    # Checking any element which
    # is not equal to i+1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1
         
    # Nothing is present return last index
    return n + 1
 
# Driver code
arr = [ 2, 3, -7, 6, 8, 1, -10, 15 ]
ans = firstMissingPositive(arr)
print(ans)

arr = [10, -2, 9, 7, 5, 6, 4, 8, 3]
ans = firstMissingPositive(arr)
print(ans)

arr = [2, 1]
ans = firstMissingPositive(arr)
print(ans)