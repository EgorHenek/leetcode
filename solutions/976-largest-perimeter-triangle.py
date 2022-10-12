class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return sum(nums[i:i+3])
        return 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.largestPerimeter([2, 1, 2]) == 5
    assert solution.largestPerimeter([1, 2, 1]) == 0
    assert solution.largestPerimeter([3, 2, 3, 4]) == 10
    assert solution.largestPerimeter([3, 6, 2, 3]) == 8
