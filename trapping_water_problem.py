'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
 
Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode
'''
    
def trap_with_pointers(height):
    if not height:
        return 0
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res

def trap(height):
    n = len(height)
    maxLeft, maxRight = [0] * n, [0] * n
    
    for i in range(1, n):
        maxLeft[i] = max(height[i-1], maxLeft[i-1])
    for i in range(n-2, -1, -1):
        maxRight[i] = max(height[i+1], maxRight[i+1])
        
    ans = 0
    for i in range(n):
        waterLevel = min(maxLeft[i], maxRight[i])
        if waterLevel >= height[i]:
            ans += waterLevel - height[i]
    return ans

if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    print(trap(height))
    print(trap_with_pointers(height))