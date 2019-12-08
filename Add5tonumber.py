def solution(N):
    retString = list()
    added = 0
    intStringified = list(str(N))
    for n in intStringified:
        if n == '-':
            return int('-5' + ''.join(intStringified[1:]))
        if int(n) <= 5:
            if added == 0:
                retString.append(str(5))
                added = 1
        retString.append(n)
    return int(''.join(retString))

def solutionImutable(N): # Not optimized solution 
    retString = ''
    added = 0
    intStringified = str(N)
    for n in intStringified:
        if n == '-':
            return int('-5' + intStringified[1:])
        if int(n) <= 5:
            if added == 0:
                retString = retString + str(5)
                added = 1
        retString = retString + n
    return int(retString)


print(solution(268))
print(solution(670))
print(solution(-999))