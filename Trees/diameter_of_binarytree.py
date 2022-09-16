'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 [Easy]

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


Example 2:

Input: root = [1,2]
Output: 1
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def diameterOfBinaryTree(root):
#     if not root:
#         return 0
#     return max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right), height(root.left) + height(root.right))

# def height(root):
#     if not root:
#         return 0
#     return 1 + max(height(root.left), height(root.right))

def diameterOfBinaryTree(root):
    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res

node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.left.left.left = TreeNode(5)
node.left.left.right = TreeNode(6)

print(diameterOfBinaryTree(node))

