'''
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, 
discarding the shortest pieces until there are none left. 
At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and 
then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.
Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.

Sample Input 0

STDIN           Function
-----           --------
6               arr[] size n = 6
5 4 4 2 2 8     arr = [5, 4, 4, 2, 2, 8]
Sample Output 0

6
4
2
1
Explanation 0

sticks-length        length-of-cut   sticks-cut
5 4 4 2 2 8             2               6
3 2 2 _ _ 6             2               4
1 _ _ _ _ 4             1               2
_ _ _ _ _ 3             3               1
_ _ _ _ _ _           DONE            DONE

'''

def cut_the_sticks(arr):
    if arr is None:
        return
    dic = dict()
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    dic = sorted(list(dic.items()))
    
    retArr = []
    n = len(arr)
    for pair in dic:
        retArr.append(n)
        n-= pair[1]
        print(pair)    
    return retArr



print(cut_the_sticks([5, 4, 4, 2, 2, 8]))
print(cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]))

