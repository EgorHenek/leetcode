class Solution:
    def arraySign(self, nums: List[int]) -> int:
        multi = reduce(lambda v,x:  v * x, nums)
        if multi > 0:
            return 1
        elif multi == 0:
            return 0
        return -1