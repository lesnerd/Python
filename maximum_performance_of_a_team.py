'''
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

[Hard] 

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
'''

import heapq

def max_performance(n, speed, efficiency, k):
    eng = []
    for eff, spd in zip(efficiency, speed):
        eng.append([eff, spd])
    eng.sort(reverse=True)

    res, speed = 0, 0
    minHeap = []
    for eff, spd in eng:
        if len(minHeap) == k:
            speed = heapq.heappop(minHeap)
        speed += spd
        heapq.heappush(minHeap, spd)
        res = max(res, eff * speed)

    return res % (10 ** 9 + 7)

def maxPerformance(n, speed, efficiency, k):
    minHeap = []
    res = sSum = 0
    for eff, spd in sorted(zip(efficiency, speed), reverse=1):
        heapq.heappush(minHeap, spd)
        sSum += spd
        if len(minHeap) > k:
            sSum -= heapq.heappop(minHeap)
        res = max(res, sSum * eff)
    return res % (10 ** 9 + 7)

print(max_performance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))