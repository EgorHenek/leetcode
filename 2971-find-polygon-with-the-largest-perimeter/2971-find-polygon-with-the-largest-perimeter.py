class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = -1
        perimeter = 0
        perimeter_count = 0
        for i, n in enumerate(nums):
            if perimeter > n:
                result = perimeter + n
                perimeter_count = i
            perimeter += n
        return result