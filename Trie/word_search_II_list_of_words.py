'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

[Hard] 

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

def findWords(board, words):
    root = TrieNode()
    for word in words:
        root.add_word(word)

    rows, cols = len(board), len(board[0])
    res, visited = set(), set()

    def dfs(r, c, node, word):
        if (r < 0 or r < 0 or r == rows or c == cols or board[r][c] not in node.children or (r, c) in visited):
            return
        visited.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.is_word:
            res.add(word)

        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r, c + 1, node, word)
        dfs(r, c - 1, node, word)
        visited.remove((r, c)) # backtrack

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "")

    return list(res)

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(findWords(board, words))