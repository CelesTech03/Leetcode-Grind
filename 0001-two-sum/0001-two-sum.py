class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}
        
        for index, element in enumerate(nums):
            complement = target - element
            if complement in values:
                return [values[complement], index]
            else:
                values[element] = index
        return []
        
        