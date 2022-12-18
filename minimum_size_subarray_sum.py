'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

[Medium]

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''
# Time complexity: O(n)
def minSubArrayLen(target, nums):
    if not nums:
        return 0

    l, r = 0, 0
    targetSum = nums[0]
    minLen = float('inf') # or len(nums) + 1
    while r < len(nums):
        if targetSum < target:
            r += 1
            if r == len(nums):
                break
            targetSum += nums[r]
        else:
            minLen = min(minLen, r - l + 1)
            targetSum -= nums[l]
            l += 1
    
    return 0 if minLen == float('inf') else minLen

def minSubArrayLen2(target, nums):
    if not nums:
        return 0

    l = 0
    targetSum = 0
    minLen = float('inf') # or len(nums) + 1

    for r in range(len(nums)):
        targetSum += nums[r]
        while targetSum >= target:
            minLen = min(minLen, r - l + 1)
            targetSum -= nums[l]
            l += 1

    return 0 if minLen == float('inf') else minLen


print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))


print(minSubArrayLen2(7, [2,3,1,2,4,3]))
print(minSubArrayLen2(4, [1,4,4]))
print(minSubArrayLen2(11, [1,1,1,1,1,1,1,1]))