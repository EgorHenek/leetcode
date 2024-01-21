class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 1
        result = mean(nums[0:k])
        current_avg = result
        while i + k <= len(nums):
            current_avg = current_avg - (float(nums[i-1]) / k) + (float(nums[i+k-1]) / k)
            if current_avg > result:
                result = current_avg
            i += 1
        return result