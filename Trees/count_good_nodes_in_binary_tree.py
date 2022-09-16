'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 [Medium]

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root):
    
    
    def dfs(root, max_val):
        if not root:
            return 0
        if root.val >= max_val:
            return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
        else:
            return dfs(root.left, max_val) + dfs(root.right, max_val)

    return dfs(root, root.val)


# def goodNodess(root):
#     def dfs(node, maxVal):
#         if not node:
#             return 0

#         res = 1 if node.val >= maxVal else 0
#         maxVal = max(maxVal, node.val)
#         res += dfs(node.left, maxVal)
#         res += dfs(node.right, maxVal)
#         return res

#     return dfs(root, root.val)

node = TreeNode(3)
node.left = TreeNode(1)
node.right = TreeNode(4)
node.left.left = TreeNode(3)
node.right.left = TreeNode(1)
node.right.right = TreeNode(5)
print(goodNodes(node))