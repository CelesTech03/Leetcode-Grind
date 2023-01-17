class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        num_flips = 0
        one = 0
        
        for i in range(len(s)):
            if s[i] == '1':
                one += 1
            else:
                num_flips += 1
            
            num_flips = min(num_flips, one)
        return num_flips