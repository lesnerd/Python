from datetime import datetime 

def First_Recurring_String(input_string):
    dic = {}
    for char in input_string:
        if char in dic:
            return char
        dic[char] = 1
    return None

def First_None_Recurring(input_string):
    dic = {}
    number  = 0
    for char in input_string:
        if char in dic:
            del dic[char]
        else:
            number += 1
            dic[char] = number
    return min(dic.keys(), key=(lambda k : dic[k]))

def main():
    #print(First_Recurring_String("abcdb"))
    print(First_None_Recurring('tbbcac'))



if __name__ == "__main__": #ifdef
    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    main()