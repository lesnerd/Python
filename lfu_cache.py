'''

'''

import collections


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.listSize = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.listSize += 1

    def remove(self, node):
        if self.listSize == 0:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev
        self.listSize -= 1
        return node

    def removeLRU(self):
        if self.listSize == 0:
            return None
        node = self.tail.prev
        return self.remove(node)

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.actual_size = 0
        self.nodeMap = {}
        self.freqMap = collections.defaultdict(DLinkedList)
        self.minFreq = 0

    def get(self, key):
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.increaseFreq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key not in self.nodeMap:
            if self.actual_size == self.capacity:
                self.removeLRU()
                self.actual_size -= 1

            node = Node(key, value)
            self.nodeMap[key] = node
            self.freqMap[1].add(node)
            self.minFreq = 1
            self.actual_size += 1
        else:
            node = self.nodeMap[key]
            node.val = value
            self.increaseFreq(node)

    def increaseFreq(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)
        if self.minFreq == freq and self.freqMap[freq].listSize == 0:
            self.minFreq += 1
        node.freq += 1
        freq = node.freq
        self.freqMap[freq].add(node)
        