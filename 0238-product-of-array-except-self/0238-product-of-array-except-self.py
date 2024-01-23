class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(0, len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result