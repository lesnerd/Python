'''
This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

[Easy]

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
'''

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mostFrequentSubtree(tree):
    if tree is None:
        return []
    res = {}
    def dfs(node):
        if node is None:
            return 0
        s = node.val + dfs(node.left) + dfs(node.right)
        if s in res:
            res[s] += 1
        else:
            res[s] = 1
        return s
    dfs(tree)
    maxCount = max(res.values())
    return [s for s in res if res[s] == maxCount]


tree = TreeNode(5, TreeNode(2), TreeNode(-5))
print(mostFrequentSubtree(tree))
tree = TreeNode(5, TreeNode(2), TreeNode(-3))
print(mostFrequentSubtree(tree))