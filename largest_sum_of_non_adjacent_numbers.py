'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, 
[2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, 
since we pick 5 and 5.
'''

def solution(n):
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return n[0]
    if len(n) == 2:
        return max(n[0], n[1])
    if len(n) == 3:
        return max(n[0] + n[2], n[1])
    size = len(n) - 1
    x1, x2, x3, x4 = 0, 1, 2, 3
    last = -1000
    ret = 0
    while x1 < size:
        if n[x1] + n[x3] > n[x2] and n[x3] > n[x4] and last + 1 != x1:
            ret += n[x1] + n[x3]
            last = x3
        elif n[x2] > n[x1]:
            ret += n[x2]
            last = x2
        else:
            ret += n[x1]
            last = x1

        if x1 + 3 <= size:
            x1 += 3
        else:
            return ret
        
        if x2 + 3 <= size:
            x2 += 3
        else:
            if last + 1 == x1:
                return ret
            else:
                ret + n[x1]
        
        if x3 + 3 <= 3:
            x3 += 3
        else:
            if last + 1 == x1:
                return ret + n[x2]
            else:
                return ret + max(n[x1], n[x2])
    return ret


print(solution([2, 4, 6, 2, 5]))
print(solution([5, 1, 1, 5]))
