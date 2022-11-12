class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        chars = {")": "(",
                "}": "{",
                 "]": "["}
        
        for p in s:
            if p in chars.values():
                stack.append(p)
            elif stack and chars[p] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
        