'''
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

[Easy] 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUnivalTree(root) -> bool:               
    def helper(rootVal, node):
        if node is None:
            return True
        if node.val != rootVal:
            return False
        return helper(rootVal, node.left) and helper(rootVal, node.right)
    return helper(root.val, root)

tree = TreeNode(1)
tree.left = TreeNode(1)
tree.right = TreeNode(1)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(1)
tree.right.right = TreeNode(1)
print(isUnivalTree(tree))

tree = TreeNode(2)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(5)
tree.left.right = TreeNode(2)
print(isUnivalTree(tree))