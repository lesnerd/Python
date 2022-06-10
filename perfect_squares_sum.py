'''
This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)

'''

def perfect_squares_sum(n):
    if n <= 0:
        n = abs(n)
    binary = format(n, "b")
    return binary.count("1")


print(perfect_squares_sum(4))
print(perfect_squares_sum(17))
print(perfect_squares_sum(18))