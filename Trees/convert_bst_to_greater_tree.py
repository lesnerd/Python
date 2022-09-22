'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
[Medium]

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root): # traverse post order
    currentSum = 0

    def dfs(node):
        if not node:
            return

        nonlocal currentSum
        dfs(node.right)
        originalNodeValue = node.val
        node.val += currentSum
        currentSum = originalNodeValue
        dfs(node.left)
    dfs(root)
    return root


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)

print(convertBST(root))