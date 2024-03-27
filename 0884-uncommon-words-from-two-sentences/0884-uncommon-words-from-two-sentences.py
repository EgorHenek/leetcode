class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = defaultdict(int)
        for word in s1.split():
            cnt[word] += 1
        for word in s2.split():
            cnt[word] += 1
        return [k for k, v in cnt.items() if v == 1]