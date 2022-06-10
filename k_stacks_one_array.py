class KStacks:
     
    def __init__(self, k, n):
        self.k = k # Number of stacks.
        self.n = n # Total size of array holding
                   # all the 'k' stacks.

        self.arr = [0] * self.n

        self.top = [-1] * self.k
 
        self.free = 0

        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1
 
    def isEmpty(self, sn):
        return self.top[sn] == -1
 
    def isFull(self):
        return self.free == -1
 
    def push(self, item, sn):
        if self.isFull():
            print("Stack Overflow")
            return
 
        # Get the first free position
        # to insert at.
        insert_at = self.free
 
        # Adjust the free position.
        self.free = self.next[self.free]
 
        # Insert the item at the free position we obtained above.
        self.arr[insert_at] = item
 
        # Adjust next to point to the old top of stack element.
        self.next[insert_at] = self.top[sn]
 
        # Set the new top of the stack.
        self.top[sn] = insert_at
 
    # Pop item from given stack number 'sn'.
    def pop(self, sn):
        if self.isEmpty(sn):
            return None
 
        # Get the item at the top of the stack.
        top_of_stack = self.top[sn]
 
        # Set new top of stack.
        self.top[sn] = self.next[self.top[sn]]
 
        # Push the old top_of_stack to the 'free' stack.
        self.next[top_of_stack] = self.free
        self.free = top_of_stack
 
        return self.arr[top_of_stack]
 
    def printstack(self, sn):
        top_index = self.top[sn]
        while (top_index != -1):
            print(self.arr[top_index])
            top_index = self.next[top_index]
 
# Driver Code
if __name__ == "__main__":
    kstacks = KStacks(3, 5) 
    kstacks.push(10, 0)
    kstacks.push(20, 0)
    kstacks.push(30, 0)
    kstacks.push(100, 1)
    kstacks.push(200, 1)
    kstacks.pop(0)
    kstacks.pop(0)
    kstacks.pop(0)
    kstacks.pop(0)
    kstacks.printstack(0)