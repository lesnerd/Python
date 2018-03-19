def Longest_Sub_Sequence(seq):
    maxCount = 0
    maxChar = None
    prevChar = None
    count = 0

    for current in seq:
        if prevChar == current:
            count += 1
        else:
            count = 1
        if maxCount < count:
            maxCount = count
            maxChar = current
        prevChar = current
    
    return {maxChar : maxCount}


def main():
    print(Longest_Sub_Sequence("AABCDDBBBEA"))


if __name__ == "__main__": #ifdef
    main()