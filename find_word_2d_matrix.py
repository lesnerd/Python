'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

def find_word_2d_matrix(matrix, word):
    row = 0
    col = 0
    word_idx = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[word_idx]:
                row = i
                col = j
                while matrix[row][col] == word[word_idx] or (row < len(matrix) - 1 and col < len(matrix[row]) - 1):
                    word_idx += 1
                    if row + 1 <= len(matrix) - 1 and matrix[row + 1][col] == word[word_idx]:
                        row += 1
                    elif col + 1 <= len(matrix[row]) - 1 and matrix[row][col + 1] == word[word_idx]:
                        col += 1
                    else:
                        row, col, word_idx = 0, 0 ,0
                        break
                    if word_idx == len(word) - 1:
                        return True
    return False

print(find_word_2d_matrix([['F', 'A', 'C', 'I'],
                            ['O', 'B', 'Q', 'P'],
                            ['A', 'N', 'O', 'B'],
                            ['M', 'A', 'S', 'S']], "FOAM"))


print(find_word_2d_matrix([['F', 'A', 'C', 'I'],
                            ['O', 'B', 'Q', 'P'],
                            ['A', 'N', 'O', 'B'],
                            ['M', 'A', 'S', 'S']], "MAST"))