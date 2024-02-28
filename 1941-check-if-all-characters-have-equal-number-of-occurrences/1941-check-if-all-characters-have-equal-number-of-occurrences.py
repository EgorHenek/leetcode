class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        prev = cnt[s[0]]
        for key in cnt:
            if cnt[key] != prev:
                return False
        return True