# https://leetcode.com/problems/single-number/
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: list[int]) -> int | None:
        nums_counts = defaultdict(int)
        for num in nums:
            nums_counts[num] += 1

        for num, count in nums_counts.items():
            if count == 1:
                return num


if __name__ == "__main__":
    s = Solution()

    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1
