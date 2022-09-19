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

Do it in-place. The board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
'''

def game_of_life(board):
    # Original | New | Temporary State
    #   0      |  0  |  0
    #   1      |  0  |  1 
    #   0      |  1  |  2
    #   1      |  1  |  3

    rows = len(board)
    cols = len(board[0])  

    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live(board, r, c)
            if board[r][c] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                board[r][c] = 3
            elif live_neighbors == 3:
                board[r][c] = 2

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] == 2 or board[r][c] == 3:
                board[r][c] = 1

    return board

def count_live(board, i, j):
    count = 0
    cols = len(board[0])
    rows = len(board)
    if i + 1 < rows and j + 1 < cols and (board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == 3): # bottom right
        count += 1
    if i + 1 < rows and j - 1 >= 0 and (board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == 3): # bottom left
        count += 1
    if i - 1 >= 0 and j + 1 < cols and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == 3): # top right
        count += 1
    if i - 1 >= 0 and j - 1 >= 0 and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == 3): # top left
        count += 1
    if j - 1 >= 0 and (board[i][j - 1] == 1 or board[i][j - 1] == 3):
        count += 1
    if j + 1 < cols and (board[i][j + 1] == 1 or board[i][j + 1] == 3):
        count += 1
    if i + 1 < rows and (board[i + 1][j] == 1 or board[i + 1][j] == 3):
        count += 1
    if i - 1 >= 0 and (board[i - 1][j] == 1 or board[i - 1][j] == 3):
        count += 1
    return count


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(game_of_life(board))