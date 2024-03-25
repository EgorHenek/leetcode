class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        delta = (sum(bobSizes) - sum(aliceSizes)) // 2
        bobSizes = set(bobSizes)
        for i in aliceSizes:
            if i + delta in bobSizes:
                return [i, i + delta]