'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
[Medilum] 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
'''

import heapq


def reorganize_string(input):
    count = {}
    for c in input:
        count[c] = count.get(c, 0) + 1

    maxHeap = [] # there is no max heap in python so we'll use min heap and negate the count
    for c, freq in count.items():
        heapq.heappush(maxHeap, (-freq, c))

    prev = None
    result = ""
    while maxHeap or prev:
        if prev and not maxHeap: # if there is no more char to add to the result but we still have a char in prev, then we can't reorganize the string
            return ""
        count, char = heapq.heappop(maxHeap)
        result += char
        count += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None
        if count < 0:
            prev = (count, char)
    
    return result

print(reorganize_string("aab"))
print(reorganize_string("aaab"))