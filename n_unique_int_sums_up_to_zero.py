'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
'''
import math

def sumZero(n: int):
    if n == 0:
        return [0]
    ret = []
    if n % 2 != 0:
        ret.append(0)
    n = math.floor(n / 2)
    for i in range(1 ,n + 1):
        ret.append(i)
        ret.append(-i)
    return ret

print(sumZero(5))