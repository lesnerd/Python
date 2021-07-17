'''
Sort an array of 0s, 1s and 2s
Difficulty Level : Medium
Last Updated : 09 Apr, 2021
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. 
The functions should put all 0s first, then all 1s and all 2s in last.
'''

def sort012(a):
    lo = 0
    mid = 0
    hi = len(a) - 1
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a
     
def printArray( a):
    for k in a:
        print(k, sep=' ')
   

arr = [2,0,1]#[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print("Array before segregation : {}".format(arr))
arr = sort012(arr)
print("Array after segregation : {}".format(arr))