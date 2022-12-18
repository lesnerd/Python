# /* say you have an array A=[11,9,2,8,10,7,3,30,4,6,20] and the code below...
#                nlogn [2,3,4,8,6...30] k = 40 | 40- 30 -11- 
#                             dict = { 0: [9], ..., 9: 0}
# our goal is to find the minimal number of elements of A, whose sum is equal or greater (>=) than some rand number.
#              [11,20,22,30,40,47,50,80,84,86,106] O(n) k = 20
#                             [60, , 58, 50,40,60,30 ,26 ,20]
# NOTE: 
# 1. A's length can be very very big (lets call it n)
# 2. m can also change and can be very big
# 3. we care about the efficiency !

# Example: 

# rand | min
# ----------
# 1000 | -1 (base case)
#    0 |  1 (base case)
#   20 |  1 === 20-11=9, 9-9= 0 sofar = 2 
#   40 |  2
#   45 |  2
   
# */ 
#for i in range(m):

# def sumUpToK(arr, k):
#     arr.sort(reverse=True) # Onlogn
#     # arr.sort() # Onlogn
#     # arr.reverse()
#     sumsArr = []
#     addition = 0
#     for i in range(len(arr)):
#         addition += arr[i]
#         sumsArr.append(addition)
    
#     sofar = 0
#     sum = k 
#     for i,v in enumerate(arr): # O(n)
#         sum -= v
#         sofar += 1
#         if sum <= 0:
#             return sofar
#     return -1

def sumUpToK(arr, k):
    arr.sort(reverse=True) # Onlogn
    sumsArr = []
    addition = 0
    for i in range(len(arr)):
        addition += arr[i]
        sumsArr.append(addition)
    
    res = find(0, len(arr), sumsArr, k)
    return res + 1

def find(left, right, nums, target, lastIdx=0):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            lastIdx = mid
            right = mid - 1
        else:
            left = mid + 1
    return lastIdx

print(sumUpToK([11,9,2,8,10,7,3,30,4,6,20] ,40))

# using System;

# class Solution
# {
#   static void Main(string[] args)
#   {
#     // input 
#     int m = 5;
#     int[] input =  new int[]{11,9,2,8,10,7,3,30,4,6,20};

#     // run it!
#     Solution sol = new Solution();
#     sol.Run(input, m);  
#   }
  
#   public void Run(int[] numbers, int m) {
#     for (int i=0; i<m; i++) {
#       int rand = GetRand();
#       int Dd123dd456
#        = GetMinElms(rand, numbers);
#       Console.WriteLine("Number of minimum elements is: " + result);
#     }   
#   }                         
  
#   private int GetRand() {
#     Random random = new Random();
#     return random.Next(100000000);
#   }
# }


