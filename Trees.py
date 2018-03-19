from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def Add(node, root):
    if root is None:
        raise ValueError('root cannot be None.')

    nodes_found = deque([root])

    while len(nodes_found) > 0:
        current_node = nodes_found.popleft()

        if current_node.left is None:
            current_node.left = node
            break
        if current_node.right is None:
            current_node.right = node
            break

        nodes_found.append(current_node.left)
        nodes_found.append(current_node.right)


def InOrderTraversal(root):
    if root is None:
        return

    if root.left is not None:
        InOrderTraversal(root.left)
    
    print(root.key, end=' ')

    if root.right is not None:
        InOrderTraversal(root.right)


def TreeDepth(root):
    if root.left == None and root.right == None:
        return 1

    return max(TreeDepth(root.left), TreeDepth(root.right)) + 1



def PrintTree(root):
    if root is None:
        return

    spaces = TreeDepth(root)

    q = deque()
    q.append(root)
    while len(q) > 0:
        levelNumber = len(q)
        startLine = True
        while levelNumber > 0:
            current_node = q.popleft()
            levelNumber = levelNumber - 1
            
            if startLine:
                for x in range(spaces):
                    print('    ', end='')
                startLine = False
                spaces = spaces - 1

            if levelNumber == 0:
                print(current_node.key, end='\n')
            else:
                print(current_node.key, end='  ')
            
            if current_node.left != None:
                q.append(current_node.left)
            if current_node.right != None:
                q.append(current_node.right)
            
        

def main():
    root = Node(8)
    keys = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    for key in keys:
        Add(Node(key), root)

    PrintTree(root)
    #InOrderTraversal(root)

  
if __name__ == "__main__": #ifdef
    main()



