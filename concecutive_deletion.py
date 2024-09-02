'''
Given string that contains ABCD
Delete all A followed by B and all C followed by D
for example:
input: CAABDABCDC -> CADC
output: CA
'''

def consecutive_deletion(s):
    input = s
    stack = []
    run = True
    while run:
        run = False
        for i in input:
            if stack and stack[-1] == 'A' and i == 'B':
                run = True
                stack.pop()
            elif stack and stack[-1] == 'C' and i == 'D':
                run = True
                stack.pop()
            else:
                stack.append(i)
        input = ''.join(stack)
        return ''.join(stack)

print(consecutive_deletion('CAABDABCDC')) # CA
# CADC