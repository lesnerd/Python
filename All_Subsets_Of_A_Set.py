from math import pow


def All_Subsets(input_array):
    subset = [None] * len(input_array)
    Helper_Set(input_array, subset, 0)


def Helper_Set(given_array, subset, i):
    if i == len(given_array):
        print(subset)
    else:
        subset[i] = None
        Helper_Set(given_array, subset, i + 1)
        subset[i] = given_array[i]
        Helper_Set(given_array, subset, i + 1)


def Print_All_Subsets_Iterative(setArr):
    numberOfRanges = int(pow(2, len(setArr)))
    for i in range(numberOfRanges):
        print("======== start of subset ========")
        for j in range(len(setArr)):
            if (i & (1 << j)):
                print(setArr[j])
        print("======== end of subset ========")


def main():
    arr = [1, 2, 3]
    # Print_All_Subsets_Iterative(arr)
    All_Subsets(arr)


if __name__ == "__main__":  # ifdef
    main()
