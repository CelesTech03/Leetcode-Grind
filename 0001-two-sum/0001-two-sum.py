class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}
        
        for index,item in enumerate(nums):
            complement = target - item
            if complement in values:
                return [values[complement], index]
            else:
                values[item] = index