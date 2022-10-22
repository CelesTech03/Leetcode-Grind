class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        if len(s) == 0 or (len(s) > 0 and not (s[0] in ['+','-'] or s[0].isdigit())):
            return 0

        value = 0
        sign = -1 if s[0] == '-' else 1
        i = 1 if not s[0].isdigit() else 0

        while i < len(s) and s[i].isdigit():
            value = (value * 10) + (ord(s[i]) - ord('0'))
            i += 1
        value *= sign

        if value < -(2**31):
            return -(2**31)
        elif value > (2**31)-1:
            return (2**31)-1

        return value  
        
#         values = {
#             "0": 0,
#             "1": 1,
#             "2": 2,
#             "3": 3,
#             "4": 4,
#             "5": 5,
#             "6": 6,
#             "7": 7,
#             "8": 8,
#             "9": 9,
#          }

#         res = 0
#         exp = 0
#         sign = 1
            
#         if not s:
#             return 0
        
#         s = s.strip()

#         if s[0] == "-":
#             sign = -1
        
#         for i in reversed(s):
#             # Change i into a int (mapping)
#             if i in values:
#                 digit = values[i]
#                 # Multiplication with 10^zeroes
#                 digit *= 10**exp
#                 # Adding it to the solution
#                 res += digit

#                 exp += 1

#         return res * sign