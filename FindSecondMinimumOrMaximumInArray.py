import sys

def FindSecondMinimum(arr):
    minVal = arr[0]
    secondMinVal = arr[1]
    for number in arr:
        if number < minVal:
            secondMinVal = minVal
            minVal = number
    return secondMinVal


print(FindSecondMinimum([1,2,3,4]), "The answer should be: ", 2)
print(FindSecondMinimum([4,3,2,1]), "The answer should be: ", 2)
print(FindSecondMinimum([9,4,7,2,1,5,0]), "The answer should be: ", 1)