'''

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
 
# function to print zigzag traversal of
# binary tree
def zigzagtraversal(root):
 
    # Base Case
    if root is None:
        return
    ans = []  # store the traversal in the ans array
    queue = [root] # use list as queue
    flag = False
    while len(queue) != 0:
 
        n = len(queue)
        level = []
        for i in range(n):
            node = queue[0]
            queue.pop(0)
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        flag = not flag
        if flag == False:
            level = level[::-1]
        for i in range(n):
 
            ans.append(level[i])
 
    return ans
 
 
# Driver program to check above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
 
v = zigzagtraversal(root)
for i in v:
    print(i,end = " ")