class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        table = {}
        
        for num in nums:
            if num not in table:
                table[num] = 1
            if table[num] > len(nums) // 2:
                return num
            else:
                table[num] += 1
                