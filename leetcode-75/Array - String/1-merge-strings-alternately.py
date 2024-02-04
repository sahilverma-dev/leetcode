# https://leetcode.com/problems/merge-strings-alternately


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = []
        totalLength = len(word1) + len(word2)
        for i in range(totalLength):
            if i < len(word1):
                temp.append(word1[i])
            if i < len(word2):
                temp.append(word2[i])

        return "".join(temp)


# Create an instance of the Solution class
solution = Solution()

# Test 1
result1 = solution.mergeAlternately("abc", "123")
print("Test 1:", result1)

# Test 2
result2 = solution.mergeAlternately("hello", "world")
print("Test 2:", result2)

# Test 3
result3 = solution.mergeAlternately("python", "java")
print("Test 3:", result3)
