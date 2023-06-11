class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Sliding window
        charSet = set()
        
        left = 0
        res = 0
        
        for right in range(len(s)):
            # While the character is in the set
            while s[right] in charSet:
                # Delete the char from the set and shift the left pointer
                charSet.remove(s[left])
                left += 1
            # If the char is not in the set then add it
            charSet.add(s[right])
            # right - next + 1 (right index minus left index + 1 (arrays start at 0)) to get the size of the window (longest length)
            res = max(res, right - left + 1)
        return res
            