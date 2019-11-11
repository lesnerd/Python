class Queue: 
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s EnQueued to queue" %str(item))

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
        item = self.Q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1
        print("%s DeQueued from queue" %str(item))
        return item

    def getQueueFront(self):
        if self.isEmpty():
            print("Empty")
            return
        item = self.Q[self.front]
        return item

    def getQueueRear(self):
        if self.isEmpty():
            print("Empty")
            return
        item = self.Q[self.rear]
        return item


if __name__ == "__main__":
    queue = Queue(3)
    queue.EnQueue(1)
    queue.EnQueue(2)
    queue.EnQueue(3)
    queue.EnQueue(4)

    print(queue.getQueueFront())
    print(queue.getQueueRear())

    queue.DeQueue()  

    print(queue.getQueueFront())
