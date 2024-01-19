class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._b_search(nums, target, 0, len(nums))

    def _b_search(self, nums: List[int], target: int, left, right) -> int:
        middle = left + ((right - left) // 2)

        if nums[middle] == target:
            return middle
        elif left == right or left == middle:
            return -1
        elif nums[middle] < target:
            return self._b_search(nums, target, middle + 1, right)
        else:
            return self._b_search(nums, target, left, middle - 1)