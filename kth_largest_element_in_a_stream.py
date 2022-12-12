'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 
[Easy]

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
'''
import heapq


class KthLargest:
    # initiate a min heap - O(n) time + remove the first k elements - O((n-k)logn) time == O(nlogn) time
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # O(n) time
        while len(self.minHeap) > self.k: # O((n-k)logn) time -> O(nlogn) time
            heapq.heappop(self.minHeap)

    # add a new element to the min heap - O(logn) time
    # pop the smallest element O(logn) time
    # over all O(mlogn) time
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(logn) time
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap) # O(logn) time
        return self.minHeap[0] # O(1) time

kLargestElem = KthLargest(3, [2, 4, 5, 8, 1, 9, 2])
print(kLargestElem.add(3))
print(kLargestElem.add(5))
print(kLargestElem.add(10))
print(kLargestElem.add(9))
print(kLargestElem.add(4))
