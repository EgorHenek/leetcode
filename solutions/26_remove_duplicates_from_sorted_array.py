from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        deleted_count = 0
        for i, n in enumerate(nums[::-1], 1):
            if len(nums) == 1:
                return 1
            if nums[-i + 1 + deleted_count] == n:
                del nums[-i + 1 + deleted_count]
                deleted_count += 1
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    l1 = [1, 1, 2]
    l2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    l3 = [1]
    l4 = [1, 1]

    assert solution.removeDuplicates(l1) == 2
    assert l1 == [1, 2]
    assert solution.removeDuplicates(l2) == 5
    assert l2 == [0, 1, 2, 3, 4]
    assert solution.removeDuplicates(l3) == 1
    assert l3 == [1]
    assert solution.removeDuplicates(l4) == 1
    assert l4 == [1]
