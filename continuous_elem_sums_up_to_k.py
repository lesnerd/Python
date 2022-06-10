'''
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
'''

def sum_up_to_k(lst, k):
    if lst is None or len(lst) == 0:
        return []
    if len(lst) == 1 and lst[0] == k:
        return [lst[0]]
    result = []
    start = 0
    end = 1
    sum_all = lst[start]
    result.append(lst[start])
    while end < len(lst):
        if sum_all + lst[end] <= k:
            sum_all += lst[end]
            result.append(lst[end])
            end += 1
        else:
            sum_all -= lst[start]
            result.remove(lst[start])
            start += 1
        if sum_all == k:
            return result
    return []

print(sum_up_to_k([1, 2, 3, 4, 5], 9))
