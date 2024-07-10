# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # brute force

        # for i, num1 in enumerate(nums):
        #     for k in range(i + 1, len(nums)):
        #         num2 = nums[k]
        #         if num1 + num2 == target:
        #             return [i, k]
        # return []

        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # optimized solutions with hashing
        hash_map = {}
        for i, num in enumerate(nums):
            hash_map[num] = i

        for i, num in enumerate(nums):
            ele = target - num
            if ele in hash_map and hash_map[ele] != i:
                return [i, hash_map[ele]]
        return []
        # Time Complexity: O(n)
        # Space Complexity: O(n)


s = Solution()

"""
Example 1:

Input: nums = , target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
print("Example 1:", s.twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
