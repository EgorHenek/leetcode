class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        non_repeatable = set()
        for n in nums:
            if n in non_repeatable:
                return n
            non_repeatable.add(n)