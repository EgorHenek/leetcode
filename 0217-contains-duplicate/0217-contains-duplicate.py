class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i in count.values():
            if i > 1:
                return True
        return False