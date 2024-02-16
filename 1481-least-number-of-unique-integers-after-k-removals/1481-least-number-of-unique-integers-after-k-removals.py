class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freq = Counter(arr)
        hq = [v for v in freq.values()]
        heapq.heapify(hq)
        for _ in range(k):
            c = heapq.heappop(hq)
            if c > 1:
                heapq.heappush(hq, c - 1)
        return len(hq)

