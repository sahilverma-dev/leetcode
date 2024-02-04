def linear_search(array, ele):
    for i in range(0, len(array)):
        if array[i] == ele:
            return i
    return -1


print("Check 1", linear_search([1, 24, 32, 56, 2], 2))
