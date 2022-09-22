'''
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

[Medium]

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1
'''

def maxFrequency(nums, k):
    nums.sort()
    l, r = 0, 0
    res, total_sum = 0, 0

    while r < len(nums):
        total_sum += nums[r]
        while nums[r] * (r - l + 1) > total_sum + k:
            total_sum -= nums[l]
            l += 1
        res = max(res, r - l + 1) # the size of the window
        r += 1
    return res

nums = [1, 1, 1, 2, 2, 4]
k = 2
print(maxFrequency(nums, k))