class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iter_t = iter(t)
        return all(char in iter_t for char in s)
