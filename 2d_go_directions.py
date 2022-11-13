"""
We have a NxN grid, turtle initial point is bottom left (1,1) looking north, turtle movement is one of: Forward one step (F), Turn left (L), Turn right (R). Grid has 4 directions: E/W/S/N.

exmaple:

input: board size is 10, movement string: "FLLFLL"
output: (1,1,N)

Visual example:

input: board size is 4, movement string: "FFFRRFLF"
output: (2,3,E)
   _______________
  |   |   |   |   |
  |___|___|___|___|
  |   |  >|   |   |
  |___|_E_|___|___|
  |   |   |   |   |
  |___|___|___|___|
  | ^ |   |   |   |
  |_N_|___|___|___|
  

"""

def say_hello():
    N = 4
    start = [1, 1]
    point = "N"
    path = "FFFRRFLF"
    for c in path:
        if c == "F":
            if point == "N" and start[1] + 1 <= N: 
                start[1] += 1
            if point == "S" and start[1] -1 > 0:
                start[1] -= 1
            if point == "W" and start[0] - 1 > 0:
                start[0] -= 1
            if point == "E"and start[0] + 1 <= N:
                start[0] += 1
        else:
            if c == "L":
                if point == "N": 
                    point = "W"
                    continue
                if point == "W": 
                    point = "S"
                    continue
                if point == "S": 
                    point = "E"
                    continue
                if point == "E": 
                    point = "N"
                    continue
            if c == "R":
                if point == "N": 
                    point = "E"
                    continue
                if point == "E": 
                    point = "S"
                    continue
                if point == "S": 
                    point = "W"
                    continue
                if point == "W": 
                    point = "N"
                    continue
    return start, point
print(say_hello())
