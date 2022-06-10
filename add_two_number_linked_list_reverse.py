'''
This problem was asked by Microsoft. [Easy]

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
'''
from re import S


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    result_tail = result
    carry = 0
            
    while l1 or l2 or carry:            
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    
                    
        result_tail.next = ListNode(out)
        result_tail = result_tail.next                      
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
            
    return result.next

l1 = ListNode(9)
l1.next = ListNode(9)
l2 = ListNode(5)
l2.next = ListNode(2)
res = addTwoNumbers(l1, l2)
# while res:
#     print(res.val, end=' ')
#     res = res.next

def print_list(l):
    if l.next is None:
        print(l.val, end=' ')
        return
    print_list(l.next)
    print(l.val, end=' ')

print_list(res)