'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

[Medium]

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
'''

def game_of_life(board):
    rows = len(board[0])
    cols = len(board)  
    new_board = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(cols):
        for j in range(rows):
            count = count_live(board, i, j)
            if board[i][j] == 1 and (count < 2 or count > 3): # Rule 1 and 3 - a live cell with fewer than 2 or more than 3 live neighbors dies
                new_board[i][j] = 0
            elif board[i][j] == 0 and count == 3: # rule 4 - dead cell with 3 live neighbors becomes live
                new_board[i][j] = 1
            elif board[i][j] == 1 and (count == 2 or count == 3): # rule 2 - live cell with 2 or 3 live neighbors lives on
                new_board[i][j] = 1

    return new_board

def count_live(board, i, j):
    count = 0
    cols = len(board) - 1
    rows = len(board[0])
    if i + 1 < rows and j + 1 < cols and board[i + 1][j + 1] == 1: # bottom right
        count += 1
    if i + 1 < rows and j - 1 >= 0 and board[i + 1][j - 1] == 1: # bottom left
        count += 1
    if i - 1 >= 0 and j + 1 < cols and board[i - 1][j + 1] == 1: # top right
        count += 1
    if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == 1: # top left
        count += 1
    if j - 1 >= 0 and board[i][j - 1] == 1:
        count += 1
    if j + 1 < cols and board[i][j + 1] == 1:
        count += 1
    if i + 1 < rows and board[i + 1][j] == 1:
        count += 1
    if i - 1 >= 0 and board[i - 1][j] == 1:
        count += 1
    return count


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(game_of_life(board))