'''
This problem was asked by Twitter.

[Medium]

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
'''

def formLargestInteger(arr):
    arr = [str(x) for x in arr]
    arr.sort(key=lambda x: x*3, reverse=True)
    # print(arr)
    return int(''.join(arr))

print(formLargestInteger([10, 7, 79, 415]))