class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        first = 0
        second = 1
        
        maxP = 0
        
        while second < len(prices):
            if prices[first] < prices[second]:
                profit = prices[second] - prices[first]
                maxP = max(maxP, profit)
            else:
                first = second
            second += 1
                
        return maxP
                
            
                
                
            