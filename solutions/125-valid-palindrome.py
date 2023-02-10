# https://leetcode.com/problems/valid-palindrome/
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(re.findall(r"[a-z0-9]", s))
        return s == s[::-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
