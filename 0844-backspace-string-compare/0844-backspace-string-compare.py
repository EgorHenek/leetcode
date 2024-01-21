class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s), len(t)

        while i >= 0 and j >= 0:
            back = 1
            while back > 0:
                i -= 1
                back += 1 if i >= 0 and s[i] == "#" else -1
            
            back = 1
            while back > 0:
                j -= 1
                back += 1 if j >= 0 and t[j] == "#" else -1
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
        
        return i < 0 and j < 0