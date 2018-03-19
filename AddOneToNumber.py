
def Add_One(given_array):
    carry = 1
    new_arr = [0] * len(given_array)
    for i in range(len(given_array) - 1, -1, -1):
        total = given_array[i] + carry
        if total == 10:
            carry = 1
        else:
            carry = 0
        new_arr[i] = total % 10

    if carry == 1:
        new_arr = [0] * len(given_array) + 1
        new_arr[0] = 1

    return new_arr


def main():
    arr = [1, 2, 3, 9]
    print(Add_One(arr))
  
if __name__ == "__main__": #ifdef
    main()
