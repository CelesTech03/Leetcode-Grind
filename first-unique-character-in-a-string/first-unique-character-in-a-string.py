class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        table = {}
        
        for i in range(0, len(s)):
            if s[i] not in table:
                table[s[i]] = True
            else:
                table[s[i]] = False
        
        for i in range(0, len(s)):
            if table[s[i]]:
                return i
        return -1