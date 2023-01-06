class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        res = 0
        ind = 0
        
        while ind < len(costs) and coins >= costs[ind]:
            coins -= costs[ind]
            ind += 1
            res += 1
            
        return res