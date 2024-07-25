class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for c in s:
            # check if its a opening pair
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            # since opening condition is full filled now the rest characters will be closing brackets or remove the corresponding open pair

            elif not stack or c != pairs[stack.pop()]:
                return False

        return len(stack) == 0


"""
You're absolutely correct that in this process, we've popped { from the stack. This is intentional, but it can be confusing at first glance.
The reason this works is:

If the brackets match, we want to remove the opening bracket from the stack because it's been "closed".
If the brackets don't match, we're going to return False anyway, so it doesn't matter that we've altered the stack.
"""


s = Solution()

print("Example 1:", s.isValid("()"))  # True
print("Example 2:", s.isValid("()[]{}"))  # True
print("Example 3:", s.isValid("(]"))  # False
