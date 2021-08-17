'''
This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, 
there must be a duplicate. Find it in linear time and space.
'''

def findDuplicate(nums):
    for i in range(0, len(nums)):
        if nums[abs(nums[i])] >= 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            print(abs(nums[i]), end=" ")

def solution2(nums):
    for i in range(0, len(nums)):
        if i + 1 == nums[i]:
            continue
        else:
            tmp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = tmp
    return nums[-1]

def solution1(nums):
    real_sum, arr_sum = 0, 0
    for i in range(0, len(nums)):
        real_sum += i

    for i in range(1, len(nums) + 1):
        arr_sum += nums[i - 1]
    return arr_sum - real_sum

print(solution1([1,3,4,2,2])) # 2
print(solution1([3,1,3,4,2])) # 3
print(solution1([1, 1])) # 1
print(solution1([1, 1, 2])) # 1
print(solution1([2, 2, 2, 2, 2])) # 2

# print(solution2([1,3,4,2,2])) # 2
# print(solution2([3,1,3,4,2])) # 3
# print(solution2([1, 1])) # 1
# print(solution2([1, 1, 2])) # 1
# print(solution2([2, 2, 2, 2, 2])) # 2

# print(findDuplicate([1,3,4,2,2])) # 2
# print(findDuplicate([3,1,3,4,2])) # 3
# print(findDuplicate([1, 1])) # 1
# print(findDuplicate([1, 1, 2])) # 1
# print(findDuplicate([2, 2, 2, 2, 2])) # 2
