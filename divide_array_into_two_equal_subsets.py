'''
This problem was asked by Microsoft. [Hard]

Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.
'''

def divide_array_into_two_equal_subsets(arr, n):
    sum = 0;
    for i in range(n):
        sum += arr[i];
    y = sum // 2 + 1;
     
    # dp[i] gives whether is it possible to get i as
    # sum of elements dd is helper variable we use dd
    # to ignoring duplicates
    dp = [False for i in range(y)]
    dd = [False for i in range(y)]
     
    # Initialising dp and dd
     
    # sum = 0 is possible
    dd[0] = True;
    for i in range(n):
       
        # updating dd[k] as True if k can be formed
        # using elements from 1 to i+1
        for j in range(y):
            if (j + arr[i] < y and dp[j]):
                dd[j + arr[i]] = True;
         
        # updating dd
        for j in range(y):
            if (dd[j]):
                dp[j] = True;
            dd[j] = False; # reset dd
         
    # checking the number from sum/2 to 1 which is
    # possible to get as sum
    for i in range(y-1, 0, -1):
        if (dp[i]):
            return (sum - 2 * i);
           
        # since i is possible to form then another
        # number is sum-i so mindifference is sum-i-i
    return 0;

'''
------------------- Different approach: -------------------
'''

def my_solution(arr, size):
    if size < 1:
        return
    arr[size - 1] = abs(arr[size] - arr[size - 1])
    my_solution(arr, size - 1)
    return arr[0]

#b = [1,6,11,5]
#b = [5,10,15,20,25]
b = [1,5,10,15,20,25]
b.sort() # n(log n)
print("My solution is: ", my_solution(b, len(b)-1)) # n(log n)

'''
------------------- Different approach: -------------------
'''
 
if __name__ == '__main__':
 
    #arr = [ 1, 5, 10, 15, 20, 25 ]
    #arr = [ 1,9,13,22,30 ]
    arr = [ 1,4,3,9 ]
    n = len(arr);
    print("The Minimum difference of 2 sets is ", divide_array_into_two_equal_subsets(arr, n));