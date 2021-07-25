'''
This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
'''
import sys

def next_sparse(number):
    for i in range(number ,sys.maxsize):
        if i & (i * 2) == 0:
            return i


print(next_sparse(6))
