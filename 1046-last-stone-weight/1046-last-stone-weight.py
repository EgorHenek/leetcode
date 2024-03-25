class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            num1 = heapq.heappop(stones)
            num2 = heapq.heappop(stones)
            diff = abs(num1 - num2)
            if diff > 0:
                heapq.heappush(stones, -diff)
        if stones:
            return -heapq.heappop(stones)
        return 0