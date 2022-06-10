'''
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

from heapq import heappush, heappop, heapify
import math

minHeap=[]
heapify(minHeap)
maxHeap=[]
heapify(maxHeap)

def insertHeaps(num):
    heappush(maxHeap,-num)                ### Pushing negative element to obtain a minHeap for
    heappush(minHeap,-heappop(maxHeap))    ### the negative counterpart
   
    if len(minHeap) > len(maxHeap):
        heappush(maxHeap,-heappop(minHeap))
     
def getMedian():
    if len(minHeap)!= len(maxHeap):
        return -maxHeap[0]
    else:
        return (minHeap[0]- maxHeap[0])/2
   
 
if __name__== '__main__':
    #A= [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    A = [2, 1, 5, 7, 2, 0, 5]
    n= len(A)
    for i in range(n):
        insertHeaps(A[i])
        print(getMedian())