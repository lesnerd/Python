'''
Maximum difference between two elements such that larger element appears after the smaller number
'''

def max_difference_bw_two_elements_larger_first(arr):
    arr_size = len(arr)
    max_diff = -1 if arr[1] - arr[0] < 0 else arr[1] - arr[0]
    min_element = arr[0]
      
    for i in range( 1, arr_size ):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
      
        if (arr[i] < min_element):
            min_element = arr[i]
    return max_diff

if __name__ == '__main__':
    arr = [2, 3, 10, 6, 4, 8, 1]
    ans = max_difference_bw_two_elements_larger_first(arr)
    assert ans == 8
    print(ans)
    arr = [7, 9, 5, 6, 3, 2]
    ans = max_difference_bw_two_elements_larger_first(arr)
    assert ans == 2
    print(ans)