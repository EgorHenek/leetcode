class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count_zeros = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[count_zeros], nums[i] = nums[i], nums[count_zeros]
                count_zeros += 1
        