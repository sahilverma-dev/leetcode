# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0

        for char in s:
            if char == "(":
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ")":
                current_depth -= 1

        return max_depth


s = Solution()
print("Example 1:", s.maxDepth("(1+(2*3)+((8)/4))+1"))  # 3
print("Example 2:", s.maxDepth("(1)+((2))+(((3)))"))  # 3
print("Example 3:", s.maxDepth("()(())((()()))"))  # 3
