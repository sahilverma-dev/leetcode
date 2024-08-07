# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            # check for operators
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            # c is a number
            else:
                stack.append(int(c))

        print(stack)
        return stack[0]


s = Solution()

print("Example 1:", s.evalRPN(["2", "1", "+", "3", "*"]))  # 9
print("Example 2:", s.evalRPN(["4", "13", "5", "/", "+"]))  # 6
print(
    "Example 2:",
    s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
)  # 22
