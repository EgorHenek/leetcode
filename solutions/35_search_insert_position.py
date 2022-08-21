from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return i


if __name__ == "__main__":
    solution = Solution()
    ll = [1, 3, 5, 6]
    assert solution.searchInsert(ll, 5) == 2
    assert solution.searchInsert(ll, 2) == 1
    assert solution.searchInsert(ll, 7) == 4
