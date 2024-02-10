class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        slow = fast = 0
        while slow < len(s):
            while fast < len(s):
                if s[slow:fast] == s[fast:slow:-1]:
                    count += 1
                fast += 1
            slow += 1
            fast = slow
        return count
            