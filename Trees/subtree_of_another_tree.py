'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

[Easy]

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''

from re import sub


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)



def sameTree(root, subRoot):
    if not root and not subRoot:
        return True

    if not root or not subRoot:
        return False

    if root.val != subRoot.val:
        return False

    return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

node = TreeNode(3)
node.left = TreeNode(4)
node.right = TreeNode(5)
node.left.left = TreeNode(1)
node.left.right = TreeNode(2)

subnode = TreeNode(4)
subnode.left = TreeNode(1)
subnode.right = TreeNode(2)

print(isSubtree(node, subnode))