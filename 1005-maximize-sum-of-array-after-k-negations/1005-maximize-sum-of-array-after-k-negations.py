class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            num = heapq.heappop(nums)
            if num >= 0:
                if k % 2 == 0:
                    return sum(nums) + num
                else:
                    return sum(nums) - num
            else:
                heapq.heappush(nums, -num)
            k -= 1
        return sum(nums)
        