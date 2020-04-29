import re
import os
import json

def isPossibelToReachTheEndOfArray(givenArray) -> bool:
    if givenArray is None:
        return False
    arrayLength = len(givenArray)
    if arrayLength == 0 or arrayLength == 1 or givenArray[0] == arrayLength:
        return True
    visitedIndexs = [None] * arrayLength
    stack = []
    stack.append(givenArray[0])
    visitedIndexs[0] = True
    while len(stack) > 0:
        currentIndex = stack.pop()
        stepBeckWards = currentIndex - givenArray[currentIndex]
        stepForward = currentIndex + givenArray[currentIndex]
        if stepForward == arrayLength - 1 or currentIndex == arrayLength - 1:
            return True
        if stepBeckWards >= 0 and visitedIndexs[stepBeckWards] is None:
            stack.append(stepBeckWards)
            visitedIndexs[stepBeckWards] = True
        if stepForward < arrayLength and visitedIndexs[stepForward] is None:
            stack.append(stepForward)
            visitedIndexs[stepForward] = True

    return False

def saveToJson():
    with open('/Users/lesnerd/Downloads/Cartica test cases - Json.json', 'w') as outfile:
        json.dump([4, 4, 1, 1, 2, 2, 1000, 1], outfile)
        json.dump([1, 2, 4, 1, 5, 100, 1, 100, 1, 1, 1, 1], outfile)
        json.dump([3, 2, 0, 1], outfile)
        json.dump([2, 0, 1, 1, 0], outfile)
        json.dump([1], outfile)
        json.dump([0], outfile)
        json.dump([4, 2, 1, 3, 2, 2, 1000, 1], outfile)
        json.dump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], outfile)
        json.dump([2, 2, 0, 1], outfile)
        json.dump([2, 0, 0, 1, 0], outfile)

def main():
    userInput = input("Please enter full file path to CVS, TSV or Json formats: ")
    if not os.path.isfile(userInput):
        print("The file could not be located")
    #print(re.split(',|\t', userInput))
    val = isPossibelToReachTheEndOfArray([4, 4, 1, 1, 2, 2, 1000, 1]) # True
    print(val)
    val = isPossibelToReachTheEndOfArray([1, 2, 4, 1, 5, 100, 1, 100, 1, 1, 1, 1]) # True
    print(val)
    val = isPossibelToReachTheEndOfArray([3, 2, 0, 1]) # True
    print(val)
    val = isPossibelToReachTheEndOfArray([2, 0, 1, 1, 0]) # True
    print(val)
    val = isPossibelToReachTheEndOfArray([1]) # True
    print(val)
    val = isPossibelToReachTheEndOfArray([0]) # True
    print(val)
    val = isPossibelToReachTheEndOfArray([4, 2, 1, 3, 2, 2, 1000, 1]) # False
    print(val)
    val = isPossibelToReachTheEndOfArray([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]) # False
    print(val)
    val = isPossibelToReachTheEndOfArray([2, 2, 0, 1]) # False
    print(val)
    val = isPossibelToReachTheEndOfArray([2, 0, 0, 1, 0]) # False
    print(val)
    val = isPossibelToReachTheEndOfArray(None) # False
    print(val)
if __name__ == "__main__":
    main()
    #saveToJson()


class PathFinderAlgo():

    def __init__ß(self,
               )

    def find(self, path,file_format):
        file