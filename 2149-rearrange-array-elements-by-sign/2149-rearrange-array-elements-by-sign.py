class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_list = []
        negative_list = []
        result = []
        for num in nums:
            if num < 0:
                negative_list.append(num)
            else:
                positive_list.append(num)
        for i in range(len(positive_list)):
            result.append(positive_list[i])
            result.append(negative_list[i])
        return result