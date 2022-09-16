'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 [Easy]

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if not q and not p:
        return True

    if not q or not p:
        return False

    if q.val != p.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

print(isSameTree(p, q))