# https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


s = Solution()
print("Example 1:", s.calPoints(["5", "2", "C", "D", "+"]))  # 30
print("Example 2:", s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print("Example 3:", s.calPoints(["1", "C"]))  # 0
