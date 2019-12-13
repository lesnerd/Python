def autobiographicalNumber(number):
    dic = dict()
    for n in str(number):
        if int(n) in dic:
            dic[int(n)] = dic[int(n)] + 1
        else:
            dic[int(n)] = 1

    idx = 0
    for n in str(number):
        if idx in dic and dic[idx] != int(n):
            return 0
        idx = idx + 1
        
    return 1


# Pass
print(autobiographicalNumber(1210)) 
print(autobiographicalNumber(2020)) 
print(autobiographicalNumber(21200))
print(autobiographicalNumber(3211000))
print(autobiographicalNumber(42101000))
print(autobiographicalNumber(521001000))
print(autobiographicalNumber(6210001000))

# Fail
print(autobiographicalNumber(112233)) 
print(autobiographicalNumber(1234567)) 
print(autobiographicalNumber(11223423)) 