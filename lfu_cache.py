'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

[Hard] 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
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
                removed = self.freqMap[self.minFreq].removeLRU()
                self.nodeMap.pop(removed.key)
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
        

lfuCache = LFUCache(2)
lfuCache.put(1, 1)
lfuCache.put(2, 2)
print(lfuCache.get(1))
lfuCache.put(3, 3)
print(lfuCache.get(2))
print(lfuCache.get(3))
lfuCache.put(4, 4)
print(lfuCache.get(1))
print(lfuCache.get(3))
print(lfuCache.get(4))