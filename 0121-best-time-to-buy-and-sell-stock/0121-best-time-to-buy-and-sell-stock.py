class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 # sell
        right = 1 # buy
        
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
                
            right += 1
        
        return maxProfit