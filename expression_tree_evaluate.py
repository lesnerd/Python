'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def evaluateExpressionTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.data)
    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.right)

    if root.data == '+':
        return left_sum + right_sum
    elif root.data == '-':
        return left_sum - right_sum
    elif root.data == '*':
        return left_sum * right_sum
    else:
        return left_sum / right_sum

if __name__ == '__main__':
 
    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('-4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')
    print (evaluateExpressionTree(root))
 
    root = None
 
    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print (evaluateExpressionTree(root))