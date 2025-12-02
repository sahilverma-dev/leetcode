from collections import defaultdict
from typing import List


def countTrapezoids(points: List[List[int]]) -> int:
    point_num = defaultdict(int)

    print(point_num)

    mod = 10**9 + 7  #  answer may be very large, return it modulo 109 + 7.
    ans, total_sum = 0, 0

    # groupig by y point bzc x will be same
    for point in points:
        point_num[point[1]] += 1

    print(point_num)

    for p_num in point_num.values():
        edge = p_num * (p_num - 1) // 2
        ans = (ans + edge * total_sum) % mod
        total_sum = (total_sum + edge) % mod
    return ans


points = [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]


print("Answer:", countTrapezoids(points=points))
