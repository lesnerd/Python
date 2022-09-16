"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""

class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.left = None
        self.right = None
 

def buildTree(preorder, inorder):
    if not preorder:
        return None
    root = Node(preorder[0])
    root_index = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:root_index+1], inorder[:root_index])
    root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])
    return root

def prInorder(node):
 
    if (node == None):
        return
         
    prInorder(node.left)
    print(node.data, end = " ")
    prInorder(node.right)

if __name__ == '__main__':
     
    mp = {}
    preIndex = 0
 
    inn = [ 'D', 'B', 'E', 'A', 'F', 'C' ]
    pre = [ 'A', 'B', 'D', 'E', 'C', 'F' ]
    lenn = len(inn)
 
    #root = buldTreeWrap(inn, pre,lenn)
    root = buildTree(pre, inn)
    # Let us test the built tree by printing
    # Inorder traversal
    print("Inorder traversal of "
          "the constructed tree is")
     
    prInorder(root)