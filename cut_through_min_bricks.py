'''
This problem was asked by LinkedIn.

A wall consists of several rows of bricks of various integer lengths and uniform height. Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks. If the line goes through the edge between two bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent the lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
The best we can we do here is to draw a line after the eighth brick, which will only require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above, return the fewest number of bricks that must be cut to create a vertical line.
'''

input_arr = [[3, 5, 1, 1],   # 3, 8, 9, 10
            [2, 3, 3, 2],    # 2, 5, 8, 10
            [5, 5],          # 5, 10
            [4, 4, 2],       # 4, 8, 10
            [1, 3, 3, 3],    # 1, 4, 7, 10
            [1, 1, 6, 1, 1]] # 1, 2, 8, 9, 10


def get_min_bricks(input):
    if input is None:
        return -1
    modified_arr = aggregated_2d_array(input)
    dic = dict()
    for row in modified_arr:
        for elem in row:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem] = dic[elem] + 1
    maximum = max(dic.values())
    return len(modified_arr) - maximum

def aggregated_2d_array(array):
    cut_arr = []
    for i in range(len(array)):
        row_sum = 0
        cols = []
        for j in range(len(array[i]) -1):
            row_sum += array[i][j]
            cols.append(row_sum)
        cut_arr.append(cols)
    return cut_arr
            

result = get_min_bricks(input_arr)
print(result)
assert result == 2