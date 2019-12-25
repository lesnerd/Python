"""
This problem was asked by Facebook.
Given a list of strictly positive integers, partition the list into 3 contiguous partitions 
which each sum up to the same value. If not possible, return null.
"""


def isSumsUptoEqualValue(arr, k):
    if arr is None:
        return None

    sum = 0
    for val in arr:
        sum += val
    if sum % k != 0:
        return None
    groupSum = sum / k
    sum = 0
    retArr = []
    tmpArr = []
    for number in arr:
        sum += number
        tmpArr.append(number)
        if sum == groupSum:
            retArr.append(tmpArr)
            sum = 0
            tmpArr = []

    return retArr


print(isSumsUptoEqualValue([3, 5, 8, 0, 8], 3))
