'''
This problem was asked by Microsoft.

Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]
Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
Recall that the median of an even-sized list is the average of the two middle numbers.
'''
# import heapq

# def medianSlidingWindow(nums, k):
# 	small, large = [], []
# 	for i, x in enumerate(nums[:k]): 
# 		heapq.heappush(small, (-x,i))
# 	for _ in range(k-(k>>1)): 
# 		move(small, large)
# 	ans = [get_med(small, large, k)]
# 	for i, x in enumerate(nums[k:]):
# 		if x >= large[0][0]:
# 			heapq.heappush(large, (x, i+k))
# 			if nums[i] <= large[0][0]: 
# 				move(large, small)
# 		else:
# 			heapq.heappush(small, (-x, i+k))
# 			if nums[i] >= large[0][0]: 
# 				move(small, large)
# 		while small and small[0][1] <= i: 
# 			heapq.heappop(small)
# 		while large and large[0][1] <= i: 
# 			heapq.heappop(large)
# 		ans.append(get_med(small, large, k))
# 	return ans

# def move(h1, h2):
# 	x, i = heapq.heappop(h1)
# 	heapq.heappush(h2, (-x, i))
	
# def get_med(h1, h2, k):
# 	return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.

# print(medianSlidingWindow([-1, 5, 13, 8, 2, 3, 3, 1], 3))
import bisect

def medianSlidingWindow(nums, k):
    win, rv = nums[:k], []
    win.sort()
    odd = k % 2
    for i, n in enumerate(nums[k:],k):
        if not odd:
            rv.append((win[k / 2]+win[k / 2 - 1]) / 2)
        else:
            rv.append(win[int((k-1)/2)])
        win.remove(nums[i-k]) 
        bisect.insort(win, nums[i])
    #rv.append((win[k/2]+win[k/2-1])/2. if not odd else win[(k-1)/2]*1.)
    if not odd:
        rv.append((win[k/2]+win[k/2-1])/2.)
    else:
        rv.append(win[int((k-1)/2)])
    return rv

print(medianSlidingWindow([-1, 5, 13, 8, 2, 3, 3, 1], 3)) # n log(k)