from typing import List


a: List[int] = [5, 2, 9, 1, 7]

n = len(a)
# buddle sort

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        # print(a[i], a[j])

print(a)
