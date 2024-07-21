class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
        return True


s = Solution()

print("Example 1:", s.isPalindrome("A man, a plan, a canal: Panama"))  # True
print("Example 2:", s.isPalindrome("race a car"))  # False
