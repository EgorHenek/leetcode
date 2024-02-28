class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        prev = 0
        for key in cnt:
            if not prev:
                prev = cnt[key]
                continue
            if cnt[key] != prev:
                return False
        return True