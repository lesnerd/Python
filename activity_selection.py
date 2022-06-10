'''
This problem was asked by Microsoft.

You are given a list of jobs to be done, where each job is represented by a start time and end time. Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.

For example, given the following jobs (there is no guarantee that jobs will be sorted):

[(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
Return:

[(1, 4),
(4, 7),
(8, 11)]
'''

def MaxActivities(arr, n):
    selected = []
     
    # Sort jobs according to finish time
    Activity.sort(key = lambda x : x[1])
     
    # The first activity always gets selected
    i = 0
    selected.append(arr[i])
 
    for j in range(1, n):
      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected
 
# Driver code
Activity = [(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)