def printSubArrays(arr, start, end): 
    if end == len(arr): 
        return
    elif start > end: 
        return printSubArrays(arr, 0, end + 1) 
    else: 
        print(arr[start:end + 1]) 
        return printSubArrays(arr, start + 1, end) 
          
arr = [1, 2, 3] 
printSubArrays(arr, 0, 0)