'''
Kadane's Algorithm is an iterative dynamic programming algorithm.
It calculates the maximum sum subarray ending at a particular position by using the maximum sum subarray ending at the previous position.
'''
import sys

def kadane_max_sum_subarray(arr):
    
    if arr is None or len(arr) == 0:
        raise ValueError('arr cannot be None or empty.')

    max_val = sys.maxsize * -1
    so_far = arr[0]
    if arr[0] > 0:
        max_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] + so_far > 0 and so_far > 0:
            if so_far + arr[i] > max_val:
                max_val = so_far + arr[i]
            so_far = so_far + arr[i]
        else:
            so_far = arr[i]
    
    return max_val

print(kadane_max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
