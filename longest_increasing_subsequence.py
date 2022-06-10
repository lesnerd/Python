'''
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

def lis(a):
    n = len(a)
    sorted_arr = sorted(list(set(a))) # nlog(n)
    sorted_length = len(sorted_arr)
 
    # Creating dp table for storing the answers of sub problems
    dp = [[-1 for i in range(sorted_length + 1)] for j in range(n + 1)]
 
    # Finding Longest common Subsequence of the two arrays
    for i in range(n + 1):
 
        for j in range(sorted_length + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i-1] == sorted_arr[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
 
 
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is ", lis(arr))

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("Length of lis is ", lis(arr))