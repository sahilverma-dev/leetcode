class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if target < sum:
                r -= 1
            elif target > sum:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


s = Solution()
print("Example 1:", s.twoSum([2, 7, 11, 15], 9))  # [1,2]
print("Example 1:", s.twoSum([2, 3, 4], 6))  # [1,3]
