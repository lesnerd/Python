'''
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def findNth(n): 
    count = 0;
      
    curr = 19;
  
    while (True): 
        sum = 0;
        x = curr;
        while (x > 0):
            sum = sum + x % 10;
            x = int(x / 10);

        if (sum == 10): 
            count+= 1; 
  
        if (count == n): 
            return curr;
          
        curr += 9;
  
    return -1; 
  
# Driver Code
print(findNth(5)); 
print(findNth(19)); 