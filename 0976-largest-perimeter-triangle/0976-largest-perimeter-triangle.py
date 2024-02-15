class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            a, b, c = (nums[d] for d in range(i - 2, i + 1))
            if a + b > c and a + c > b and b + c > a:
                return a + b +c
        return 0