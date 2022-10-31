'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

[Easy]

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root, x: int, y: int) -> bool:
    def dfs(node, parent, depth, mod):
        if node:
            if node.val == mod:
                return parent, depth
            else:
                return dfs(node.left, node, depth+1, mod) or dfs(node.right, node, depth+1, mod)
    xParent, xDepth =  dfs(root, root, 1, x)
    yParent, yDepth =  dfs(root, root, 1, y)
    return xParent != yParent and xDepth == yDepth

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
print(isCousins(tree, 4, 3))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right = TreeNode(3)
tree.right.right = TreeNode(5)
print(isCousins(tree, 5, 4))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(4)
print(isCousins(tree, 2, 3))