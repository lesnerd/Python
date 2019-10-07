def delete_nth(order,max_e):
    dic = {}
    lst = list()
    for number in order:
        if number not in dic:
            dic[number] = 1
        else:
            if dic[number] < max_e:
                dic[number] +=1
                
    for number in order:
        if number in dic:
            lst.append(number)
            if dic[number] > 0:
                dic[number] -=1
                if dic[number] == 0:
                    del dic[number]

    return lst


print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))