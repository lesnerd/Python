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


def topView(root):
    from collections import defaultdict

    queue = [(root, 0)]
    hashtable = defaultdict(lambda: [])
    for node, level in queue:  # level=x-coordinator
        if node != None:
            # hashtable, collect node data with the same level#
            hashtable[level].append(node.info)
            # add node in sublevel to queue
            queue.extend([(node.left, level-1), (node.right, level+1)])
    if hashtable != None:
        for level in range(min(hashtable.keys()), max(hashtable.keys())+1):  # simple for loop
            print(hashtable[level][0], end=' ')  # TOPVIEW
    else:
        return None


tree = BinarySearchTree()

arr = [1, 2, 5, 3, 6, 4]

for i in range(len(arr)):
    tree.create(arr[i])

topView(tree.root)
