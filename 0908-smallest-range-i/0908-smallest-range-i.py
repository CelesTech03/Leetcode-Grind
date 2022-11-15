class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        if len(nums)==1:
            return 0
        else:
            min_val=min(nums)+k
            max_val=max(nums)-k
        if min_val>max_val:
            return 0
        else:
            return max_val-min_val