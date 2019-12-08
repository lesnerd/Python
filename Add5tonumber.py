def solution(N):
    retString = list()
    added = 0
    intStringified = list(str(N))
    isNegative = 0
    for n in intStringified:
        if n == '-' or isNegative == 1:
            isNegative = 1
            if n == '-':
                retString.append(n)
                continue
            elif int(n) >= 5 and added == 0:
                retString.append(str(5))
                added = 1
            retString.append(n)
            # return int('-5' + ''.join(intStringified[1:]))
        elif int(n) <= 5:
            if added == 0:
                retString.append(str(5))
                added = 1
            retString.append(n)
        else:
            retString.append(n)

    if added == 0:
        retString.append(str(5))
    return int(''.join(retString))


print(solution(268))  # 5268
print(solution(670))  # 6750
print(solution(-999))  # -5999
print(solution(-444))  # -4445
