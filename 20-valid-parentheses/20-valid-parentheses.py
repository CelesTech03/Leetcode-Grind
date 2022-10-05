class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        chars = { ")": "(", 
                        "]": "[", 
                        "}": "{" }
        
        for p in s:
            if p in chars.values():
                stack.append(p)
            elif stack and chars[p] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
        
        
        
        
#         # O(n) TS
#         stack = []
#         closeToOpen = { ")": "(", 
#                        "]": "[", 
#                        "}": "{" }
#         for c in s:
#             if c in closeToOpen:
#                 # stack[-1] last value on stack
#                 if stack and stack[-1] == closeToOpen[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         # Returns true if stack is empty
#         return True if not stack else False
        