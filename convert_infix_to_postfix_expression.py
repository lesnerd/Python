'''
For example,

Input:  A*B+C
Output: AB*C+
 
Input:  (A+B)*(C/D)
Output: AB+CD/*
 
Input:  A*(B*C+D*E)+F
Output: ABC*DE*+*F+
 
Input:  (A+B)*C+(D-E)/F+G
Output: AB+C*DE-F/+G+
'''

import sys
from collections import deque
 
def prec(c):
    if c == '*' or c == '/':
        return 3
 
    if c == '+' or c == '-':
        return 4
 
    if c == '&':
        return 8
 
    # Bitwise XOR (exclusive or)
    if c == '^':
        return 9
 
    # Bitwise OR (inclusive or)
    if c == '|':
        return 10
 
    # add more operators if needed
    return sys.maxsize        # for opening bracket '('
 
 
def isOperand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
 
 
# Function to convert an infix expression to a postfix expression.
# This function expects a valid infix expression
def infixToPostfix(infix):
    # base case
    if not infix or not len(infix):
        return True
 
    # create an empty stack for storing operators
    s = deque()
 
    # create a string to store the postfix expression
    postfix = ''
 
    # process the infix expression from left to right
    for c in infix:

        if c == '(':
            s.append(c)
 
        elif c == ')':
            # pop tokens from the stack until the corresponding opening bracket '('
            # is removed. Append each operator at the end of the postfix expression
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()
 
        # Case 3. If the current token is an operand, append it at the end of the
        # postfix expression
        elif isOperand(c):
            postfix += c
 
        # Case 4. If the current token is an operator
        else:
            # remove operators from the stack with higher or equal precedence
            # and append them at the end of the postfix expression
            while s and prec(c) >= prec(s[-1]):
                postfix += s.pop()
 
            # finally, push the current operator on top of the stack
            s.append(c)
 
    # append any remaining operators in the stack at the end of the postfix expression
    while s:
        postfix += s.pop()
 
    return postfix
 
 
if __name__ == '__main__':
    infix = 'A*(B*C+D*E)+F'
    postfix = infixToPostfix(infix)
    print(postfix)