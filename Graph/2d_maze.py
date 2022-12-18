'''
Given a matrix of m x n elements and a starting point. Find the shortest path to reach a given destination point from the starting point. 
The path can only be created by moving in the cells that have a value of 1. 
The path cannot contain any cell with a value of 0. The path can only be created in the 4 directions (up, down, left, right) from the current cell.
Return the length of the shortest path or -1 if no path exists.

[Medium]
'''

def shortest_path(matrix, start, end):
    if not matrix or not matrix[0]:
        return -1
    m, n = len(matrix), len(matrix[0])
    visited = set()
    visited.add((start[0], start[1]))
    def dfs(x, y):
        if x == end[0] and y == end[1]:
            return True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                if dfs(nx, ny):
                    return True
                visited.remove((nx, ny))
        return False
    dfs(start[0], start[1])
    return len(visited) - 1

matrix =    [[1, 0, 1, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 1, 0]]

print(shortest_path(matrix, (0, 0), (1, 3)))

matrix =    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(shortest_path(matrix, (3, 0), (4, 9)))
