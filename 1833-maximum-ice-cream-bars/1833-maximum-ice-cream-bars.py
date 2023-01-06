class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        bought = 0
        
        for cost in costs:
            if cost > coins:
                break
            else:
                coins -= cost
                bought += 1
                
        return bought