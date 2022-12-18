'''
Same as lfu_cache.py, but using a OrderedDict instead of DLinkedList.
'''

import collections

class Node:
    def __init__(self, value, count):
        self.value = value
        self.count = count

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.minCount = 0
        self.nodeKeyMap = {} # { key : Node }
        self.nodeCountMap = collections.defaultdict(collections.OrderedDict) # { count : { key : Node }}

    def get(self, key):
        if key not in self.nodeKeyMap:
            return -1
        
        node = self.nodeKeyMap[key]
        del self.nodeCountMap[node.count][key]

        if len(self.nodeCountMap[self.minCount]) == 0:
            del self.nodeCountMap[self.minCount]

        node.count += 1
        self.nodeCountMap[node.count][key] = node

        if len(self.nodeCountMap[self.minCount]) == 0:
            self.minCount += 1 
        
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.nodeKeyMap:
            self.nodeKeyMap[key].value = value
            self.get(key)
            return

        if self.capacity == len(self.nodeKeyMap):
            lfuItem = self.nodeCountMap[self.minCount].popitem(last=False)
            del self.nodeKeyMap[lfuItem[0]]

        newNode = Node(value, 1)
        self.nodeKeyMap[key] = newNode
        self.nodeCountMap[1][key] = newNode
        self.minCount = 1


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