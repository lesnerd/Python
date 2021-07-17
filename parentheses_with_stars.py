'''
This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
'''

def is_balanced(str):
    if str is None:
        False
    joker = 0
    stack = []
    for i, c in enumerate(str):
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 and joker == 0 and i == len(str) - 1:
                return False
            elif len(stack) == 0 and joker > 0:
                joker -= 1
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if item == '(':
                    continue
        else: # if c == '*':
            joker += 1
            if len(stack) == 0:
                continue
            itm = stack.pop()
            if len(stack) == 0 and itm == '(' and i < len(str) - 1:
                stack.append(itm)
            elif itm == '(':
                joker -= 1
            elif itm == '*':
                while itm == '*':
                    itm = stack.pop()
            else:
                stack.append(c)

    return len(stack) == 0


print(is_balanced("(()*")) # true
print(is_balanced("(*)")) # true
print(is_balanced("(***)")) # true
print(is_balanced(")*(")) #false
print(is_balanced("*")) # true
print(is_balanced("***(*)")) # true
print(is_balanced("(*)****")) # true
print(is_balanced("*)")) # true
print(is_balanced("*)")) # true
print(is_balanced("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")) #true
