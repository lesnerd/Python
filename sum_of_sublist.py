'''
This problem was asked by Goldman Sachs. [Hard]

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
'''

def sublistSum(arr, i, j):
    tmp = 0
    sumsLst = []
    for num in arr:
        tmp += num
        sumsLst.append(tmp)

    if i < 0 or j >= len(sumsLst) or i > j:
        return -1

    if i == 0:
        return sumsLst[j - 1]
    else:
        return sumsLst[j - 1] - sumsLst[i - 1]

print(sublistSum([1,2,3,4,5], 1, 3))
print(sublistSum([1,2,3,4,5], 0, 3))
print(sublistSum([1,2,3,4,5], 1, 1))
print(sublistSum([1,2,3,4,5], 0, 4))

#  0,1,2,3,4
# [1,2,3,4,5]
# [1,3,6,10,15]

