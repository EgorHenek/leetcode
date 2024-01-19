class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self._b_search(0, len(nums))

    def _b_search(self, left, right) -> int:
        middle = left + ((right - left) // 2)

        if self.nums[middle] == self.target:
            return middle
        elif left == right or left == middle:
            return -1
        elif self.nums[middle] < self.target:
            return self._b_search(middle, right)
        else:
            return self._b_search(left, middle)