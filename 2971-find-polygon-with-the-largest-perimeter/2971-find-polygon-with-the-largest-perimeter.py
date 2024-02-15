class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = -1
        perimeter = 0
        for n in nums:
            if perimeter > n:
                result = perimeter + n
            perimeter += n
        return result