class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        
        for i in range(len(s)):
            # [s[i]] = character at key 
            # Everytime we see a char we increment count of that character by one. Have to use get and put default value at 0 if nothing exists yet
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True