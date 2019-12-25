from queue import *


class Node:
    def __init__(self, value: int, next_node: "Node" = None):
        self.value = value
        self.next = next_node


class SpecialLikedList:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            localRoot = self.root
            prev = None
            while localRoot != None:
                prev = localRoot
                localRoot = localRoot.next
            prev.next = Node(item)

    def sortedInsert(item):
        pass

    def printList(self):
        if self.root is None:
            print("Nothing to print.")
        head = self.root
        while head != None:
            print(head.value, end=' ')
            head = head.next

    def removeKthNodeFromEnd(self, k):  # Do this in one pass
        if k == 0 or self.root is None:
            print("Illegal operation.")
            return
        queue = Queue(maxsize=k+1)
        head = self.root
        while head != None:
            if queue.full():
                queue.get()
                queue.put(head)
            else:
                queue.put(head)
            head = head.next

        item = None
        if not queue.empty():
            item = queue.get()
        if item.next.next is None or item.next is None:
            item.next = None
        toRefer = item.next.next
        item.next = toRefer


lst = SpecialLikedList()
lst.insert(1)
lst.insert(2)
lst.insert(3)
lst.insert(4)
lst.insert(5)
print("\nAfter insertion: ")
lst.printList()

lst.removeKthNodeFromEnd(2)
print("\nAfter removing the K-th element: ")
lst.printList()
