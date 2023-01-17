class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        
        product_so_far = 1
        
        minimum_i = 0
        subarrays = 0
        total = 0
        
        for i in range(N):
            # Calc product so far, add to subarray
            product_so_far *= nums[i]
            subarrays += 1
            
            # While loop to increase mini and decrease subarrays
            while product_so_far >= k and minimum_i <= i:
                product_so_far /= nums[minimum_i]
                minimum_i += 1
                subarrays -=1
            
            # if product_so_far < k
            # Add subarrays to total
            if product_so_far < k:
                total += subarrays
        
        return total