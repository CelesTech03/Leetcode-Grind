class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        
        for index, a in enumerate(nums):
            # If the value is the same as the one before, continue.
            # This avoids duplicates
            if index > 0 and a == nums[index - 1]:
                continue
                
            left, right = index + 1, len(nums) - 1
            
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return res