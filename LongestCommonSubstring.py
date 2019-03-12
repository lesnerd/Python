# from array import *

# "ABAZDC", "BACBAD" => "BAD"
# "AGGTAB", "GXTXAYB" => "GTAB"
# "aaaa", "aa" => "aa"
# "", "..." => ""
# "ABBA", "ABCABA" => "ABBA"


def LongestCommonSubstring(str1, str2):
    arr = [[0] * (len(str1) + 1) for c in range(len(str2) + 1)]

    for i in range(len(str2) + 1):
        for j in range(len(str1) + 1):
            if(i == 0 or j == 0):
                arr[i][j] = 0
            elif(str1[j-1] == str2[i-1]):
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    # return arr
    # Following code is used to print LCS
    index = arr[len(arr)-1][len(arr[0])-1]

    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    j = len(arr) - 1
    i = len(arr[0]) - 1
    while i > 0 and j > 0:
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if str1[i-1] == str2[j-1]:
            lcs[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif arr[i-1][j] > arr[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("LCS of " + str1 + " and " + str2 + " is " + "".join(lcs))


def main():
    LongestCommonSubstring("ABBA", "ABCABA")


if __name__ == "__main__":
    main()
