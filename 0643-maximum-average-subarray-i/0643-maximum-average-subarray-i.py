class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = mean(nums[0:k])
        current_avg = result
        for i in range(1, len(nums) - k + 1):
            current_avg = current_avg - (float(nums[i-1]) / k) + (float(nums[i+k-1]) / k)
            result = max(current_avg, result)
        return result