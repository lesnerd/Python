def runAsSnailInTwoDArray(array):
    x = len(array) 
    y = len(array[0]) 
    row = col = 0
    retString = ''
    while row < x and col < y:
        for i in range(col, y):
            retString = retString + str(array[row][i]) + ' '
        row += 1

        for i in range(row, x):
            retString = retString + str(array[i][y - 1]) + ' '
        y -= 1

        if row < x:
            for i in range(y - 1, col - 1, -1):
                retString = retString + str(array[x - 1][i]) + ' '
            x -= 1
        
        if col < y:
            for i in range(x - 1, row - 1, -1):
                retString = retString + str(array[i][col]) + ' '
            col += 1
    return retString



arr1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(runAsSnailInTwoDArray(arr1))

arr2 = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 

print(runAsSnailInTwoDArray(arr2))