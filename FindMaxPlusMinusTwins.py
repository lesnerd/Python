def solution(A):
    dic = dict()
    biggestNumber = 0
    for num in A:
        if num <= 0:
            if abs(num) in dic:
                if biggestNumber < abs(num):
                    biggestNumber = abs(num)
                    dic[abs(num)] = 0
            dic[num] = 1
        else:
            if -1 * num in dic:
                if biggestNumber < num:
                    biggestNumber = num
                    dic[num] = 0
            dic[num] = 1

    return biggestNumber


        


print(solution([3,2,-2,5,-3]))
print(solution([1,1,2,-1,2,-1]))
print(solution([1,2,3,-4]))