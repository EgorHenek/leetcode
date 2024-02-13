class Solution:
    def firstUniqChar(self, s: str) -> int:
        dummy = Counter(s)
        for i in range(len(s)):
            if dummy[s[i]] == 1:
                return i
        return -1