def nextBiggestIntWithSameNoOf1Bits(number):
    numberOf1Bits = bin(number).count("1")
    number += 1
    while numberOf1Bits != bin(number).count("1"):
        number += 1
    return number


print(nextBiggestIntWithSameNoOf1Bits(6))  # 6 -> 0110 ====> 9 -> 1001
print(nextBiggestIntWithSameNoOf1Bits(8))  # 8 -> 1000 ====> 16 -> 10000
