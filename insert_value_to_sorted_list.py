'''
Given a linked list which is sorted, how will you insert in sorted way
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        elif self.head.value >= new_node.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next


llist = LinkedList()
new_node = Node(5)
llist.sorted_insert(new_node)
new_node = Node(10)
llist.sorted_insert(new_node)
new_node = Node(7)
llist.sorted_insert(new_node)
new_node = Node(3)
llist.sorted_insert(new_node)
new_node = Node(1)
llist.sorted_insert(new_node)
new_node = Node(9)
llist.sorted_insert(new_node)