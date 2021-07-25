'''
This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
'''
 
# Utility function to create new node
class newNode:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Returns count of nodes in BST in
# range [low, high]
def getCount(root, low, high):
     
    if root == None:
        return 0
 
    if root.data <= high and root.data >= low:
        return (root.data + getCount(root.left, low, high) +
                getCount(root.right, low, high))
 
    elif root.data < low:
        return getCount(root.right, low, high)
 
    else:
        return getCount(root.left, low, high)
 
if __name__ == '__main__':
     
    root = newNode(10)
    root.left = newNode(5)
    root.right = newNode(50)
    root.left.left = newNode(1)
    root.right.left = newNode(40)
    root.right.right = newNode(100)
     
    # Let us constructed BST shown in above example
    #     10
    #     / \
    # 5     50
    # /     / \
    # 1     40 100
    l = 5
    h = 45
    print("Count of nodes between [", l, ", ", h,"] is ", getCount(root, l, h))