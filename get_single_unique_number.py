'''
This problem was asked by Google. (Hard)

Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

INT_SIZE = 32
 
def getSingle(arr, n) :
     
    result = 0
     
    # Iterate through every bit
    for i in range(0, INT_SIZE) :
         
        # Find sum of set bits
        # at ith position in all
        # array elements
        sm = 0
        x = (1 << i)
        for j in range(0, n) :
            if (arr[j] & x) :
                sm = sm + 1
                 
        # The bits with sum not
        # multiple of 3, are the
        # bits of element with
        # single occurrence.
        if ((sm % 3)!= 0) :
            result = result | x
     
    return result
     
# Driver program
arr = [6, 1, 3, 3, 3, 6, 6]
n = len(arr)
print("The element with single occurrence is ", getSingle(arr, n))