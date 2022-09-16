'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
        
    tmp = root.right
    root.right = root.left
    root.left = tmp
    
    invertTree(root.right)
    invertTree(root.left)
    
    return root

def printTree(root):
    if not root:
        return None
    print(root.val, end=' ')
    printTree(root.left)
    printTree(root.right)

node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)

printTree(node)
invertTree(node)
print()
printTree(node)