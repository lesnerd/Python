'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

also added min()
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.max_stack) == 0 or val >= self.max_stack[-1]:
            self.max_stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return None
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def get_max(self):
        if len(self.max_stack) == 0:
            return None
        return self.max_stack[-1]

    def get_min(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]

if __name__ == '__main__':
    stack = Stack()   
    stack.push(3)
    stack.push(5) 
    stack.get_min()
    stack.push(2)
    stack.push(1)
    stack.get_min()     
    stack.pop()
    stack.get_min()
    stack.pop() 