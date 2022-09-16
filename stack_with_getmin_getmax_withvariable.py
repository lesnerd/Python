'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

also added min()
'''

class Node:
    def __init__(self, value, min, max):
        self.value = value
        self.min = min
        self.max = max

class MinMaxStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(Node(value= val, min= val, max= val))
        else:
            last_node = self.stack[-1]
            if last_node.min > val:
                new_node = Node(value= val, min= val, max= last_node.max)
            elif last_node.max < val:
                new_node = Node(value= val, min= last_node.min, max= val)
            self.stack.append(new_node)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop().value

    def get_max(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1].max

    def get_min(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1].min

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1].value

if __name__ == '__main__':
    stack = MinMaxStack()   
    stack.push(3)
    stack.push(5) 
    stack.get_min()
    stack.push(2)
    stack.push(1)
    stack.get_min()     
    stack.pop()
    stack.get_min()
    stack.pop()