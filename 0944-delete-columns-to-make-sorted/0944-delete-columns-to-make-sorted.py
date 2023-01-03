class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        
        deletions = 0
        
        for col in zip(*strs):
            if list(col) != sorted(col):
                deletions += 1
        return deletions