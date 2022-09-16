'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 [Medium]

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
'''
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def rightSideView(root):
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        right_side = None
        q_size = len(q)
        for i in range(q_size):
            node = q.popleft()
            if node:
                right_side = node
                q.append(node.left)
                q.append(node.right)

        if right_side:
            res.append(right_side.val)
    return res

def leftSideView(root):
    res = []
    stack = []  # append, pop
    if root is not None:
        stack.append(root)
    while len(stack) > 0:
        left_side = None
        size = len(stack)
        idx = 0
        while size > 0:
            node = stack.pop(0)
            if idx == 0:
                left_side = node
                idx += 1
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            size -= 1
        if left_side:
            res.append(left_side.val)
    return res

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(7)
node.right.right = TreeNode(4)

print(rightSideView(node))
print(leftSideView(node))