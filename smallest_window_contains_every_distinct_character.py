"""
This problem was asked by Amazon.

Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""
from collections import defaultdict

def smallest_window_contains_every_distinct_character(strr):
    n = len(strr)
    if n <= 1:
        return strr
 
    dist_count = len(set([x for x in strr]))
 
    curr_count = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n

    for j in range(n):
        curr_count[strr[j]] += 1
 
        if curr_count[strr[j]] == 1:
            count += 1
 
        if count == dist_count:
            while curr_count[strr[start]] > 1:
                if curr_count[strr[start]] > 1:
                    curr_count[strr[start]] -= 1
 
                start += 1
  
            len_window = j - start + 1
 
            if min_len > len_window:
                min_len = len_window
                start_index = start

    return str(strr[start_index: start_index + min_len])
 

print(smallest_window_contains_every_distinct_character("jiujitsu"))
#print(smallest_window_contains_every_distinct_character("aabcbcdbca"))