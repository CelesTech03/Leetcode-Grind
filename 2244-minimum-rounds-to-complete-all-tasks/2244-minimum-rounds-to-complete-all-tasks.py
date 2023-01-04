class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        counts = dict()
        
        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1
        
        res = 0
        for key, value in counts.items():
            if value == 1:
                return -1
            elif value % 3 == 0:
                res += (value // 3)
            else:
                res += (value //3) + 1
        
        return res
                