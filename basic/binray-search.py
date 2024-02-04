def binary_search(array, ele):
    high, low = len(array) - 1, 0

    while high >= low:
        mid = int((high + low) / 2)
        if array[mid] == ele:
            return mid
        elif array[mid] > ele:
            high = mid - 1
        elif array[mid] < ele:
            low = mid + 1

    return -1  # if element not found


# Sorted array
array = [1, 2, 3, 4, 5, 6, 7]

print("Check 1:", binary_search(array, 5))
