def sortStack(s):
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortedInsert(s, temp)


def sortedInsert(s, number):
    if len(s) == 0 or number > s[-1]:
        s.append(number)
    else:
        temp = s.pop()
        sortedInsert(s, number)
        s.append(temp)


stack = [-3, 14, 18, -5, 30]
print(stack)
sortStack(stack)
print(stack)