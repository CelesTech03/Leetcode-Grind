class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}
        
        for index, ele in enumerate(nums):
            complement = target - ele
            if complement in values:
                return values[complement], index
            else:
                values[ele] = index
                
        
    