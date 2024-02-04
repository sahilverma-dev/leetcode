def bubble_sort(array):

    n = len(array) - 1

    for i in range(0, n):
        for j in range(0, n - i):
            if array[j] >= array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


unsorted_array = [5, 2, 8, 1, 7, 3, 6, 4]


print("Sorted Array:", bubble_sort(unsorted_array))
