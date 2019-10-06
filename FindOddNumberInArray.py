def find_it(seq):
    dictionary = {}
    for number in seq:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
            
    for key in dictionary:
        if dictionary[key] % 2 != 0:
            return key

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))