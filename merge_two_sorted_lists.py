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
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 is None and list2 is None:
                return None
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            
            merged_list = ListNode()
            tail = merged_list
            while list1 and list2:               
                if list1.val < list2.val:
                    tail.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    tail.next = ListNode(list2.val)
                    list2 = list2.next
                tail = tail.next
            
            while list1:
                tail.next = ListNode(list1.val, None)
                list1 = list1.next
                tail = tail.next
            while list2:
                tail.next = ListNode(list2.val, None)
                list2 = list2.next
                tail = tail.next
            return merged_list.next


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
merged_list = Solution().mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, sep=' ', end=' ')
    merged_list = merged_list.next