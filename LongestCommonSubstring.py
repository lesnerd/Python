# from array import *

# "ABAZDC", "BACBAD" => "BAD"
# "AGGTAB", "GXTXAYB" => "GTAB"
# "aaaa", "aa" => "aa"
# "", "..." => ""
# "ABBA", "ABCABA" => "ABBA"

class Val:
    def __init__(self, value, string):
        self.value = value
        self.string = string

def LongestCommonSubstring_length(str1, str2):
    dp = [[Val(0, "")] * (len(str2) + 1) for i in range(len(str1) + 1)]

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = Val(dp[i + 1][j + 1].value + 1, dp[i + 1][j + 1].string + str1[i])
                # dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = Val(max(dp[i + 1][j].value, dp[i][j + 1].value), dp[i + 1][j].string if dp[i + 1][j].value > dp[i][j + 1].value else dp[i][j + 1].string)
                # dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]

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
    # LongestCommonSubstring("ABBA", "ABCABA")
    # obj = LongestCommonSubstring_length("ABBA", "ABCABA")
    # print(f"Value: {obj.value}, String: {obj.string}")
    obj = LongestCommonSubstring_length("ABAZDC", "BACBAD") # returns ABAD
    print(f"Value: {obj.value}, String: {obj.string[::-1]}")


if __name__ == "__main__":
    main()
