class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        best_sum = float('inf')
        
        nums.sort()
        
        for index in range(0, len(nums) - 2):
            
            if nums[index] == nums[index-1] and index > 0:
                continue
                
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                
                threeSum = nums[index] + nums[left] + nums[right]
                
                if threeSum == target:
                    return threeSum
                
                if abs(target - threeSum) < abs(target - best_sum):
                    best_sum = threeSum
                
                if threeSum <= target:
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1
                
                else:
                    right -= 1
        
        return best_sum
                
                
            
            