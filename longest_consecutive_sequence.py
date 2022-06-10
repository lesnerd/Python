'''
This problem was asked by Microsoft. [Medium]

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

def longest_consecutive_sequence(arr):
    s = set()
    ans = 0
 
    for ele in arr:
        s.add(ele)

    for i in range(len(arr)):
 
        # if current element is the starting
        # element of a sequence
        if (arr[i]-1) not in s:
 
            # Then check for next elements in the
            # sequence
            j = arr[i]
            while(j in s):
                j += 1
 
            # update  optimal length if this length
            # is more
            ans = max(ans, j-arr[i])
    return ans

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))