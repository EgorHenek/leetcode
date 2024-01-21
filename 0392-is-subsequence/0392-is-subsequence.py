class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for i in range(len(t)):
            if counter < len(s) and s[counter] == t[i]:
                counter += 1
        return counter == len(s)
