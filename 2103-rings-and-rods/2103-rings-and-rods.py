class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = defaultdict(lambda: {"R": 0, "G": 0, "B": 0})
        for i in range(0, len(rings), 2):
            ring, rod = rings[i], rings[i+1]
            cnt[rod][ring] += 1
        result = 0
        for rod in cnt:
            if min(cnt[rod].values()):
                result += 1
        return result