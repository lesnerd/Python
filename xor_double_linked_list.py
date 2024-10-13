'''
This problem was asked by Google. [Hard]

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

A -> B -> C -> D
XOR LINKED LIST

Data        A          B           C           D 
Next    0 XOR B     A XOR C     B XOR D     C XOR 0

'''
def Node():
    def __init__(self, value: int, both: int = 0):
        self.value = value
        self.both = both

def xor_double_linked_list():
    def __init__(self, head: Node = None):
        self.head = head

    def add(self, element):
        #both = prev xor next
        if self.head == None:
            self.head = Node(element)
            self.head.both = 0 ^ random.int()
            return
        current = self.head
        prev = 0
        

    def get(self, index):
        pass

        
