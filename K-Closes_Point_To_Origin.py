from math import sqrt, pow
import heapq

def K_Closest_Point_To_Origin(points, k): #Sqrt( (x2−x1)2 + (y2−y1)2 )
    distances_for_the_points = Get_Distances(points) # O(n)
    print("Original points are now distances: {op}".format(op=distances_for_the_points), end='\n')
    max_heap = []
    for i in range(len(distances_for_the_points) - 1):
        if i < k:
            heapq.heappush(max_heap, distances_for_the_points[i]) 
        else:
            heapq._heapify_max(max_heap)
            current_max = heapq._heappop_max(max_heap)
            if distances_for_the_points[i] < current_max:
                heapq.heappush(max_heap, distances_for_the_points[i]) #O(log k)
            else:
                heapq.heappush(max_heap, current_max)

    return max_heap #print O(k)
# In total O(n + log(k) + k)



def Get_Distances(points):
    result = [] * len(points)
    for point in points:
        result.append(sqrt(pow(point[0], 2) + pow(point[1], 2)))

    return result

def main():
    points  = [(-2, -4), (0, -2), (-1,0), (3, -5), (-2, -3) ,(3,2)]
    print("Original points are: {op}".format(op=points), end='\n')
    k = 3
    closest_points = K_Closest_Point_To_Origin(points, k)
    print("These are the {k} closest points: {cp}".format(k=k, cp=closest_points), end='\n')
  
if __name__ == "__main__": #ifdef
    main()
