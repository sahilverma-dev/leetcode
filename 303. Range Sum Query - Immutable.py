from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.ps = []
        c = 0
        for i in nums:
            c += i
            self.ps.append(c)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.ps[right]
        leftSum = self.ps[left - 1] if left > 0 else 0

        return rightSum - leftSum


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
# return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5))
# return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5))
# return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
