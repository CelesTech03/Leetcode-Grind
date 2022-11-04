class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        N = len(board[0])
        M = len(board)
        P = len(word)
        
        def helper(r,c,pos):
            if pos >= P:
                return True
            elif 0 <= r < M and 0 <= c < N and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                if (helper(r - 1,c,pos+1) or 
                helper(r + 1,c,pos+1) or 
                helper(r,c - 1,pos+1) or 
                helper(r,c + 1,pos+1)):
                    return True
                board[r][c] = temp
            return False
                
        for r in range(M):
            for c in range(N):
                if helper(r,c,0):
                    return True
        return False
        
        
#         ROWS, COLS = len(board), len(board[0])
#         path = set()
        
#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
#             if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
#                 return False
                
#             path.add((r, c))
#             res = (dfs(r + 1, c, i + 1) or
#                   dfs(r - 1, c, i + 1) or
#                   dfs(r, c + 1, i + 1) or
#                   dfs(r, c - 1, i + 1))
#             path.remove((r, c))
#             return res
            
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c, 0): return True
        
#         return False