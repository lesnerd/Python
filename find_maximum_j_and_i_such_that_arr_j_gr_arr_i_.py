'''
Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
'''

def find_maximum(arr):
    n = len(arr)
    LMin = [0] * n
    RMax = [0] * n

    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])

    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1]);


    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1

    return maxDiff

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
ans = find_maximum(arr)
assert ans == 6
print(ans)

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
ans = find_maximum(arr)
assert ans == 8
print(ans)

arr = [1, 2, 3, 4, 5, 6]
ans = find_maximum(arr)
assert ans == 5
print(ans)

arr = [6, 5, 4, 3, 2, 1]
ans = find_maximum(arr)
assert ans == 0
print(ans)

arr = [7, 3, 1, 8, 9, 10, 4, 5, 6]
ans = find_maximum(arr)
assert ans == 7
print(ans)