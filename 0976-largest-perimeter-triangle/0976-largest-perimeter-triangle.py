class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(2, len(nums)):
            a, b, c = (nums[d] for d in range(i - 2, i + 1))
            if a + b > c and a + c > b and b + c > a:
                ans = a + b +c
                return ans
        return ans