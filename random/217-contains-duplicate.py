# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # brute force
        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if num1 == num2 and i != j:
        #             return True
        # return False

        # optimized solution with hash map
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                return True
            else:
                hash_map[num] = i

        return False


"""

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

s = Solution()
print("Example 1:", s.containsDuplicate([1, 2, 3, 1]))  # true
print("Example 2:", s.containsDuplicate([1, 2, 3, 4]))  # false
print("Example 3:", s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true
print("Example 4:", s.containsDuplicate([3, 3]))  # false
