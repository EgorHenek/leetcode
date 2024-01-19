from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = defaultdict(list)
        for i, num in enumerate(nums):
            numsDict[num].append(i)
        
        for num, i in numsDict.items():
            diff = target - num
            if num == diff:
                if len(i) >= 2:
                    return [i[0], i[1]]
                continue
            if diff in numsDict:
                return [i[0], numsDict[diff][0]]
        