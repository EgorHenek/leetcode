class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        n = len(heights)
        
        for i in range(1, n):
            climb = heights[i] - heights[i - 1]

            if climb <= 0:
                continue
            
            if climb > 0:
                heapq.heappush(min_heap, climb)
            
            if len(min_heap) > ladders:
                brick_need = heapq.heappop(min_heap)
                bricks -= brick_need
            
            if bricks < 0:
                return i - 1
        
        return n - 1
