def isSafe(mat, r, c):
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print() 
 
def nQueen(mat, r):
    if r == len(mat):
        printSolution(mat)
        return
 
    for i in range(len(mat)):
        # if no two queens threaten each other
        if isSafe(mat, r, i):
            # place queen on the current square
            mat[r][i] = 'Q'
            # recur for the next row
            nQueen(mat, r + 1)
            # backtrack and remove the queen from the current square
            mat[r][i] = '–'


# =============================================================================
def solveNQeens(n):
    column = set()
    posDiagnal = set()
    negDiagnal = set()

    result = []
    board = [["_"] * n for i in range(n)]

    def backTrack(row):
        if row == n:
            solution = [ "".join(r) for r in board]
            result.append(solution)
            return
        
        for col in range(n):
            if col in column or row + col  in posDiagnal or row - col in negDiagnal:
                continue

            column.add(col)
            posDiagnal.add(row + col)
            negDiagnal.add(row - col)
            board[row][col] = "Q"

            backTrack(row + 1)

            column.remove(col)
            posDiagnal.remove(row + col)
            negDiagnal.remove(row - col)
            board[row][col] = "_"
    backTrack(0)
    return result
 
 
if __name__ == '__main__':
 
    print(solveNQeens(4))
    # # `N × N` chessboard
    # N = 4
 
    # # `mat[][]` keeps track of the position of queens in
    # # the current configuration
    # mat = [['–' for x in range(N)] for y in range(N)]
 
    # nQueen(mat, 0)