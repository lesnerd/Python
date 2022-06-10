'''
This problem was asked by Microsoft. [Medium]

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
'''

def find_starting_indices(string, pattern):
    result = []
    for i in range(len(string)):
        if string[i:i+len(pattern)] == pattern:
            result.append(i)
    return result

print(find_starting_indices("abracadabra", "abr"))