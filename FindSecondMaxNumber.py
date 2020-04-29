import sys

def find_second_max_number(arr):
    if arr is None:
        return -1
    largest = -sys.maxsize - 1
    second_largest = -sys.maxsize - 1
    for number in arr:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

    return second_largest


print(find_second_max_number([0, 1, 2, 3, 13, 8, 5]))