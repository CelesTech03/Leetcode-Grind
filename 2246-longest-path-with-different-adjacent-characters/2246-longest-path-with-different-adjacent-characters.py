class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        
        graph = defaultdict(list)
        
        for index, parent in enumerate(parent):
            graph[parent].append(index)
            
        ans = 1
        
        def dfs(node):
            nonlocal ans
            
            longest = second_longest = 0
            
            for child in graph[node]:
                path_length = dfs(child)
                
                if s[child] != s[node]:
                    if path_length > longest:
                        second_longest = longest
                        longest = path_length
                    elif path_length > second_longest:
                        second_longest = path_length
                
            ans = max(ans, longest + second_longest + 1)
            
            return longest + 1
        
        dfs(0)
        return ans