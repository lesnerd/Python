# Python code implementation
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count_nodes(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def shuffle_linked_list(head):
    length = count_nodes(head)
    indices = list(range(length))
    random.shuffle(indices)
    
    shuffled_head = ListNode()
    current = shuffled_head
    
    node = head
    for idx in indices:
        for _ in range(idx):
            node = node.next
        current.next = ListNode(node.val)
        current = current.next
        node = head
    
    return shuffled_head.next