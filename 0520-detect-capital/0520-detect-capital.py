class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        
        return True if word.isupper() or word.islower() or word[:1].isupper and word[1:].islower() else False