'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

[Medium]

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

def fourSum(nums, target):
    nums.sort() # make sure all duplicates are next to each other O(nlogn)
    res, quad = [], []

    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return
        l, r = 0, len(nums) - 1
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                res.append(quad + [nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                r -= 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
    kSum(4, 0, target)
    return res

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))