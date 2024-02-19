class Solution:
    def maxPower(self, s: str) -> int:
        counter = 1
        result = 0
        if len(s) == 1:
            return 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
            else:
                if counter > result:
                    result = counter
                counter = 1
        if counter > result:
            result = counter
        return result
        