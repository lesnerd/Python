class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    stack = []  # append, pop
    if root is not None:
        stack.append(root)
    while len(stack) > 0:
        size = len(stack)
        while size > 0:
            node = stack.pop(0)
            print(node.info, end=' ')
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            size -= 1
        print('')
        # print(stack, end=' ')


tree = BinarySearchTree()

arr = [1, 2, 5, 3, 6, 4]

for i in range(len(arr)):
    tree.create(arr[i])

levelOrder(tree.root)
