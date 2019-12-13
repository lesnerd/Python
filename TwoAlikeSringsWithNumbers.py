def similarTwoStrings(fullString, str2):
    secondStr = ''
    for c in str2:
        if c.isdigit():
            for i in range(int(c)):
                secondStr = secondStr + '*'
        else:
            secondStr = secondStr + c

    if len(secondStr) != len(fullString):
        return 0
    for i in range(len(fullString) - 1):
        if fullString[i] != secondStr[i] and secondStr[i] != '*':
            return 0
    return 1





print(similarTwoStrings("apple", "a4"))
print(similarTwoStrings("apple", "a2le"))

print(similarTwoStrings("apple", "a2"))
print(similarTwoStrings("apple", ""))