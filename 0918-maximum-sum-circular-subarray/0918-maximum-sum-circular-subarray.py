class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curMax, maxSum, curMin, minSum, total = -inf, -inf, inf, inf, 0
        
        for num in nums:
            curMax = max(num, curMax + num)
            maxSum = max(maxSum, curMax)
            
            curMin = min(num, curMin + num)
            minSum = min(minSum, curMin)
            
            total += num
            
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum