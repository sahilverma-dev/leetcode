# https://leetcode.com/problems/build-array-from-permutation/description/


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])
        return ans


s = Solution()

print("Example 1:", s.buildArray([0, 2, 1, 5, 3, 4]))  # [0,1,2,4,5,3]
print("Example 2:", s.buildArray([5, 0, 1, 2, 3, 4]))  # [4,5,0,1,2,3]
