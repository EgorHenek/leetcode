class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        cantidate = 0

        for num in nums:
            if counter == 0:
                candidate = num
            
            if candidate == num:
                counter += 1
            else:
                counter -= 1
        
        return candidate