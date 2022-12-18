'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
[Medium]

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    
    def valid(root, left, right):
        if not root:
            return True

        if not (root.val < right and root.val > left):
            return False

        return valid(root.left, left, root.val) and valid(root.right, root.val, right)
    return valid(root, float('-inf'), float('inf'))


node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(7)
node.right.left = TreeNode(4)
node.right.right = TreeNode(8)
print(isValidBST(node))
