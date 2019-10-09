def persistence(n):
    times = 0
    number = str(n)
    while len(number) > 1:
        newNum = 1
        for n in number:
            newNum *= int(n)
        number = str(newNum)
        times += 1
        if number == 1:
            return times
    return times


print(persistence(39))
print("Shoud be: %s" % 3)
print(persistence(4))
print("Shoud be: %s" % 0)
print(persistence(25))
print("Shoud be: %s" % 2)
print(persistence(999))
print("Shoud be: %s" % 4)