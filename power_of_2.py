import math
 
# Function to check
# Log base 2
def Log2(x):
    if x == 0:
        return false;
 
    return (math.log10(x) /
            math.log10(2));
 
# Function to check
# if x is power of 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)));
 
# Driver Code
if(isPowerOfTwo(31)):
    print("Yes");
else:
    print("No");
 
if(isPowerOfTwo(64)):
    print("Yes");
else:
    print("No");
     

# Function to check if x is power of 2
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True

# Other way
def isPowerOfTwo (x):
 
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not(x & (x - 1))) )