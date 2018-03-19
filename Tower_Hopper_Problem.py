def Is_Hoppable(towers):
    current = 0
    while True:
        if  current >= len(towers):
            return True
        if towers[current] == 0:
            return False
        current = Next_Step(current, towers)


def Next_Step(i, towers):
    max_index = 0
    for s in range(towers[i]):
        if i + towers[s + i] > max_index:
            max_index = towers[s + i] + i
    return max_index 

    

def Is_Hoppable_Iterative(arr):
	limit = len(arr)
	for i in range(len(arr) -1, -1, -1):
		if arr[i] + i  >= limit:
			limit = i
			if i == 0:
				return True
	
	return False



def main():
    #print(Is_Hoppable([4, 2, 0, 0, 2, 0]))
    #print(Is_Hoppable([4, 6, 0, 0, 1, 0]))
    #print(Is_Hoppable_Iterative([4, 2, 0, 0, 2, 0]))
    print(Is_Hoppable_Iterative([4, 6, 0, 0, 2, 0]))


if __name__ == "__main__": #ifdef
    main()