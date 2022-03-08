
def isPower_of_Three(n):
 
    if (n <= 0):
        return False
    if (n % 3 == 0):
        return isPower_of_Three(n // 3)
    if (n == 1):
        return True
    return False

# Other way
def check(n):
    """ The maximum power of 3 value that
       integer can hold is 1162261467 ( 3^19 ) ."""
    return 1162261467 % n == 0


num1 = 2
if (isPower_of_Three(num1)):
    print("Yes")
else:
    print("No")
     
num2 = 6
if (isPower_of_Three(num2)):
    print("Yes")
else:
    print("No")