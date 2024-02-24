class Solution:
    def replaceDigits(self, s: str) -> str:
        result = []
        for i in range(1, len(s), 2):
            result.append(s[i-1])
            result.append(chr(ord(s[i-1]) + int(s[i])))
        if len(s) % 2:
            result.append(s[-1])
        return "".join(result)