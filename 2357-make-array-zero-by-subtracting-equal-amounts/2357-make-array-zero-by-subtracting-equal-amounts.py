class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            if nums[-1] <= 0:
                return cnt
            if nums[i] <= 0:
                continue
            for j in range(len(nums), i, -1):
                nums[j - 1] -= nums[i]
            cnt += 1
        return cnt