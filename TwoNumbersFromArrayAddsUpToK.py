def DoesAddsUpToK(arr, k):
    dic = {}
    for num in arr:
        if num in dic:
            return True
        dic[k-num] = 1
    return False


def main():
    print(DoesAddsUpToK([10, 15, 3, 7], 10))


if __name__ == "__main__":  # ifdef
    main()
