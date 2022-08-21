from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in range(-len(nums), 0):
            if nums[num] == val:
                del nums[num]
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    l1 = [3, 2, 2, 3]
    assert solution.removeElement(l1, 3) == 2
    assert l1[:2] == [2, 2]
    l2 = [0, 1, 2, 2, 3, 0, 4, 2]
    assert solution.removeElement(l2, 2) == 5
    assert l2[:5] == [0, 1, 3, 0, 4]
