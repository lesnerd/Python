'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

[Medium]

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
'''

def maximalSquare(matrix):
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = {}
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if i + 1 >= rows or j + 1 >= cols:
                dp[(i, j)] = 1 if matrix[i][j] == "1" else 0
            elif matrix[i][j] == "1":
                dp[(i, j)] = 1 + min(dp.get((i + 1, j), matrix[i + 1][j]), dp.get((i, j + 1), matrix[i][j + 1]), dp.get((i + 1, j + 1), matrix[i + 1][j + 1]))
            else:
                dp[(i, j)] = 0
    return max(dp.values()) ** 2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))
matrix = [["0","1"],["1","0"]]
print(maximalSquare(matrix))
matrix = [["0"]]
print(maximalSquare(matrix))
matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
print(maximalSquare(matrix))