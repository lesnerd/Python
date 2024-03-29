'''
You are given an array of non-negative integers arr and a start index. When you are at an index i, 
you can move left or right by arr[i]. Your task is to figure out if you can reach value 0.

Example 1:

    Input: arr = [3, 4, 2, 3, 0, 3, 1, 2, 1], start = 7
    Output: true
    Explanation: left -> left -> right
'''

def solution(arr, start):
    memo = {}
    return dfs(arr, start, memo)

def dfs(arr, i, memo):
    if i < 0 or i >= len(arr):
        return False 
    if arr[i] == 0:
        return True
    if i in memo:
        return memo[i]
    memo[i] = False 
    if dfs(arr, i - arr[i], memo):
        return True
    if dfs(arr, i + arr[i], memo):
         return True
    return False

# Can be reached from index 0 to index len(arr) - 1. Time complexity: O(n)
def can_jump_greedy(arr):
    goal = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] + i >= goal:
            goal = i
        
    return goal == 0



print(solution([3, 4, 2, 3, 0, 3, 1, 2, 1], 7))
