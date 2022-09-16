'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
'''

def partition_string_labels(s):
    last_index = {c : i for i, c in enumerate(s)} # O(n) each char to its last index
    result = []
    size = end = 0
    for i, c in enumerate(s): # O(n)
        end = max(end, last_index[c]) # O(1)
        size += 1

        if i == end:
            result.append(size)
            size = 0
    return result

print(partition_string_labels("ababcbacadefegdehijhklij"))