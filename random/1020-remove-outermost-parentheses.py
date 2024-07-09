# https://leetcode.com/problems/remove-outermost-parentheses/description/


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        return "s"


s = Solution()
print("Example 1:", s.removeOuterParentheses("(()())(())"))  # ()()()
print("Example 2:", s.removeOuterParentheses("(()())(())(()(()))"))  # ()()()()(())
print("Example 3:", s.removeOuterParentheses("()()"))  # ""
