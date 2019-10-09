def largestRange(arr):
    dic = {}
    ret = []
    maxLength = 0
    for number in arr:
	    if number not in dic:
		    dic[number] = True
    for number in arr:
        if dic[number] in dic and dic[number] == False:
            continue
        dic[number] = False
        less = number - 1
        more = number + 1
        currentLength = 1
        while less in dic:
            if dic[less] == True:
                dic[less] = False
            else:
                break
            less -= 1
            currentLength += 1
        while more in dic:
            if dic[more] == True:
                dic[more] = False
            else:
                break
            more += 1
            currentLength += 1
        if currentLength > maxLength:
            maxLength = currentLength
            ret = [less + 1, more - 1]
    return ret


#print(largestRange([4, 2, 1, 3, 6]))
#print([1, 4])
print(largestRange([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))
print([-7, 7])