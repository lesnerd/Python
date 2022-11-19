'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

[Easy] - with hash table, O(n) time and O(n) space
[Medium] - with remembering the majority element, O(n) time and O(1) space

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

def majority_element(elements):
    if elements is None or len(elements) == 0:
        raise ValueError('elements cannot be None or empty.')

    count = 1
    majority_element = elements[0]
    for i in range(1, len(elements)):
        if count == 0:
            majority_element = elements[i]
            count = 1
            continue
        if elements[i] == majority_element:
            count += 1
        else:
            count -= 1
    return majority_element
        

print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([3,2,3]))