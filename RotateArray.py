def rotate_array_left(arr, k):
    k = k % len(arr)
    for i in range(k):
        temp = arr[0] 
        for i in range(len(arr)-1): 
            arr[i] = arr[i + 1] 
        arr[len(arr)-1] = temp
    return arr

def rotate_array_right(arr, k):
    k = k % len(arr)
    for i in range(k):
        temp = arr[len(arr)-1] 
        for i in reversed(range(len(arr))): 
            arr[i] = arr[i - 1] 
        arr[0] = temp
    return arr



print(rotate_array_left([1, 2, 3, 4, 5, 6, 7, 8], 3))
#print(rotate_array_left([7, 7, 3, 5], 2)) 
print(rotate_array_right([1, 2, 3, 4, 5, 6, 7, 8], 3))
#print(rotate_array_left([7, 7, 3, 5], 2)) 







