
FibArray = [0,1] 
  
def fibonacci(n): 
    if n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
  
def fibonacciIterative(n):
    previousNumber = 0
    previousPreviousNumber = 0
    currentNumber = 1
    for i in range(1, n-1):
        previousPreviousNumber = previousNumber
        previousNumber = currentNumber
        currentNumber = previousNumber + previousPreviousNumber
    return currentNumber

print(fibonacci(6)) 
print(fibonacciIterative(6))