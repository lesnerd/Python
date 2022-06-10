"""
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

def permute(arr, left, size):
    if left==size:
        print(arr)
    else:
        for i in range(left, size):
            arr[left], arr[i] = arr[i], arr[left]
            permute(arr, left + 1, size)
            arr[left], arr[i] = arr[i], arr[left] # backtrack
 
# Driver program to test the above function
string = "ABC"
size = len(string)
arr = list(string)
permute(arr, 0, size)

# def permute(s, answer):
#     if (len(s) == 0):
#         print(answer, end = "  ")
#         return
     
#     for i in range(len(s)):
#         ch = s[i]
#         left_substr = s[0:i]
#         right_substr = s[i + 1:]
#         rest = left_substr + right_substr
#         permute(rest, answer + str(ch))
 
# answer = ""
# permute([1,2,3], answer)