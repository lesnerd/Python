'''
Implementing a minimum heap
https://www.youtube.com/watch?v=t0Cq6tVNRBA
'''

class MinimumHeap:
    def __init__(self):
        self.heap = []

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.heap)

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self.heap)

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.heap[self.getParentIndex(index)]

    def swap(self, indexOne, indexTwo):
        self.heap[indexOne], self.heap[indexTwo] = self.heap[indexTwo], self.heap[indexOne]

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def poll(self):
        if self.heap:
            item = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.heapifyDown()
            return item
        else:
            return None

    def add(self, item):
        self.heap.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heap) - 1
        while self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex
            if self.heap[index] < self.heap[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    