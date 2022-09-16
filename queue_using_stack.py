'''
Implement a queue using the stack data structure
'''
from collections import deque
 
class Queue:
    s = deque()
 
    def __init__(self):
        self.s = deque()
 
    def enqueue(self, data):
        self.s.append(data)
 
    # Remove an item from the queue
    def dequeue(self):
        # if the stack is empty
        if not self.s:
            print('Underflow!!')
            exit(0)
 
        # pop an item from the stack
        top = self.s.pop()
 
        # if the stack becomes empty, return the popped item
        if not self.s:
            return top
 
        # recur
        item = self.dequeue()
 
        # push popped item back into the stack
        self.s.append(top)
 
        # return the result of dequeue() call
        return item
 
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
    q = Queue()
 
    # insert the above keys into the queue
    for key in keys:
        q.enqueue(key)
 
    print(q.dequeue())        # print 1
    print(q.dequeue())        # print 2
 