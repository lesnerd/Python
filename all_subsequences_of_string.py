'''
This problem was asked by Microsoft. [Easy]

Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:


x
y
z
xy
xz
yz
xyz
Note that zx is not a valid subsequence since it is not in the order of the given string.
'''

def printSubsequence(input, output):
    if len(input) == 0:
        print(output, end=' ')
        return
 
    printSubsequence(input[1:], output+input[0])

    printSubsequence(input[1:], output)
 
 
output = ""
input = "xyz"
 
printSubsequence(input, output)
 