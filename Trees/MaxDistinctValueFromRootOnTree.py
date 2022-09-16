class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
  
def largestUinquePathUtil(node, m): 
    if (not node): 
        return len(m)  
  
    if node.data in m: 
        m[node.data] += 1
    else: 
        m[node.data] = 1
  
    max_path = max(largestUinquePathUtil(node.left, m),  largestUinquePathUtil(node.right, m))  
  
    m[node.data] -= 1

    if (m[node.data] == 0):  
        del m[node.data]  
    return max_path 
  

def largestUinquePath(node): 
    if (not node): 
        return 0  
    Hash = {} 
    return largestUinquePathUtil(node, Hash) 
  
if __name__ == '__main__': 
    root = newNode(1)  
    root.left = newNode(2)  
    root.right = newNode(3)  
    root.left.left = newNode(4)  
    root.left.right = newNode(5)  
    root.right.left = newNode(6)  
    root.right.right = newNode(7)  
    root.right.left.right = newNode(8)  
    root.right.right.right = newNode(9)  
  
    print(largestUinquePath(root)) 
  