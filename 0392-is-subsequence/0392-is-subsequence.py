class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return all(char in t for char in s)
