from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            if nums[index1] > target:
                continue
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3, 2, 4], 6))
