class Solution:
    def singleNumber(self, nums: list[int]) -> int | None:
       return reduce(lambda total, x: total ^ x, nums)