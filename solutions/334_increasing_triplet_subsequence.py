class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert solution.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert solution.increasingTriplet([2, 1, 5, 0, 4, 6]) is True
    assert solution.increasingTriplet([0, 4, 2, 1, 0, -1, -3]) is False
