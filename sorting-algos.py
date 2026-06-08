from typing import List


arr = [5, 2, 9, 1, 7]


n = len(arr)
# buddle sort

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a[i], a[j])

# insertion sort
for i in range(1, n - 1):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
