class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        heap = []
        for key, v in freq_table.items():
            if len(heap) == k:
                heappushpop(heap, (v, key))
            else:
                heappush(heap, (v, key))
        ans = []
        while k > 0:
            k -= 1
            ans.append(heappop(heap)[1])
        return ans