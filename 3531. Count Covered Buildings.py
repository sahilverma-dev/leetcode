from typing import List


def countCoveredBuildings(n: int, buildings: List[List[int]]) -> int:
    covered = 0
    building_set = {(x, y) for x, y in buildings}

    for x, y in buildings:
        up = any((x, yy) in building_set for yy in range(y + 1, n + 1))
        down = any((x, yy) in building_set for yy in range(1, y))
        left = any((xx, y) in building_set for xx in range(1, x))
        right = any((xx, y) in building_set for xx in range(x + 1, n + 1))

        if up and down and left and right:
            covered += 1

    return covered


print(
    "Example 1:",
    countCoveredBuildings(n=3, buildings=[[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]),
)  # 1

print(
    "Example 2:",
    countCoveredBuildings(n=3, buildings=[[1, 1], [1, 2], [2, 1], [2, 2]]),
)  # 0

print(
    "Example 3:",
    countCoveredBuildings(n=5, buildings=[[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]),
)  # 1
