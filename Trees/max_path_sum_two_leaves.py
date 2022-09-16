'''
This question was asked by Microsoft.

Find the maximum possible sum from one leaf node to another. 
'''

import sys

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

 
def maxPathSumUtil(root, res):
    if root is None:
        return 0

    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)
 
    if root.left is not None and root.right is not None:
        res[0] = max(res[0], ls + rs + root.data)
        return max(ls, rs) + root.data
 
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data
 

# root = Node(-15)
# root.left = Node(5)
# root.right = Node(6)
# root.left.left = Node(-8)
# root.left.right = Node(1)
# root.left.left.left = Node(2)
# root.left.left.right = Node(6)
# root.right.left = Node(3)
# root.right.right = Node(9)
# root.right.right.right = Node(0)
# root.right.right.right.left = Node(4)
# root.right.right.right.right = Node(-1)
# root.right.right.right.right.left = Node(10)
root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(-20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);

res = [-sys.maxsize - 1]
maxPathSumUtil(root, res)
print ("Max pathSum of the given binary tree is", res[0])