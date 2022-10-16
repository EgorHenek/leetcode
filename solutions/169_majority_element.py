class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    solution = Solution()

    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([1]) == 1
