'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

[Easy]

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''

def merge_two_sorted_arrays(list1, list2):
    if list1 is None and list2 is None:
        return None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    l1, l2 = 0, 0
    merged_list = []
    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            merged_list.append(list1[l1])
            l1 += 1
        else:
            merged_list.append(list2[l2])
            l2 += 1
    if l1 < len(list1):
        merged_list.extend(list1[l1:])
    if l2 < len(list2):
        merged_list.extend(list2[l2:])
    return merged_list

print(merge_two_sorted_arrays([1,2,4], [1,3,4]))
print(merge_two_sorted_arrays([], []))
print(merge_two_sorted_arrays([], [0]))
print(merge_two_sorted_arrays([1, 3, 5], [2, 4, 6]))


