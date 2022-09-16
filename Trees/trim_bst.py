'''
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

[Medium]

Example 1:

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]


Example 2:

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def trimBST(node, low, high):
    if not node:
        return None
    if node.val < low:
        return trimBST(node.right, low, high)
    if node.val > high:
        return trimBST(node.left, low, high)
    node.left = trimBST(node.left, low, high)
    node.right = trimBST(node.right, low, high)
    return node


root = Node(3)
root.left = Node(1)
root.left.right = Node(2)
root.right = Node(4)

print(trimBST(root, 1, 2))