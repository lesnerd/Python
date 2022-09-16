'''
Given a Binary Tree and a number k, remove all nodes that lie only on root to leaf path(s) of length smaller than k. If a node X lies on multiple root-to-leaf paths and if any of the paths has path length >= k, then X is not deleted from Binary Tree. In other words a node is deleted if all paths going through it have lengths smaller than k.

Consider the following example Binary Tree 

               1
           /      \
         2          3
      /     \         \
    4         5        6
  /                   /
 7                   8 
Input: Root of above Binary Tree
       k = 4

Output: The tree should be changed to following  
           1
        /     \
      2          3
     /             \
   4                 6
 /                  /
7                  8
There are 3 paths 
i) 1->2->4->7      path length = 4
ii) 1->2->5        path length = 3
iii) 1->3->6->8    path length = 4 
There is only one path " 1->2->5 " of length smaller than 4.  
The node 5 is the only node that lies only on this path, so 
node 5 is removed.
Nodes 2 and 1 are not removed as they are parts of other paths
of length 4 as well.

If k is 5 or greater than 5, then whole tree is deleted. 

If k is 3 or less than 3, then nothing is deleted.
'''

class newNode: 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None
          
# Utility method that actually removes 
# the nodes which are not on the pathLen >= k.
# This method can change the root as well. 
def removeShortPathNodesUtil(root, level, k) :
  
    # Base condition 
    if (root == None) :
        return None
  
    # Traverse the tree in postorder fashion 
    # so that if a leaf node path length is 
    # shorter than k, then that node and all 
    # of its descendants till the node which  
    # are not on some other path are removed. 
    root.left = removeShortPathNodesUtil(root.left, 
                                         level + 1, k) 
    root.right = removeShortPathNodesUtil(root.right, 
                                          level + 1, k) 
  
    # If root is a leaf node and it's level 
    # is less than k then remove this node. 
    # This goes up and check for the ancestor 
    # nodes also for the same condition till
    # it finds a node which is a part of other 
    # path(s) too. 
    if (root.left == None and
        root.right == None and level < k) : 
        return None
      
    # Return root 
    return root 
  

def removeShortPathNodes(root, k) :
    pathLen = 0
    return removeShortPathNodesUtil(root, 1, k) 
  
# Method to print the tree in
# inorder fashion. 
def printInorder(root) :  
    if (root) :     
        printInorder(root.left) 
        print(root.data, end = " " )
        printInorder(root.right) 
      
if __name__ == '__main__':
    k = 4
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 
    root.left.left.left = newNode(7) 
    root.right.right = newNode(6) 
    root.right.right.left = newNode(8) 
    print("Inorder Traversal of Original tree" ) 
    printInorder(root) 
    print()
    print("Inorder Traversal of Modified tree" ) 
    res = removeShortPathNodes(root, k) 
    printInorder(res)