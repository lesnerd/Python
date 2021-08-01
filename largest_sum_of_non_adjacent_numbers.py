'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5.
'''

def solution(n):
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return n[0]
    if len(n) == 2:
        return max(n[0], n[1])
    size = len(n)
    x1, x2, x3 = 0, 1, 2
    last = -1
    end1, end2, end3 = False, False, False
    ret = 0
    while x1 < size:
        if n[x1] + n[x3] > n[x2]:
            ret += n[x1] + n[x3]
            last = x3
        else:
            ret += n[x2]
            :w
            last = x2

        if x1 + 3 >= size:
            x1 += 3
        else:
            end1 = True
        if x2 + 3 >= size:
            x2 += 3
        else:
            end2 = True
        if x3 + 3 >= 3:
            x3 += 3
        else:
            end3 = True

