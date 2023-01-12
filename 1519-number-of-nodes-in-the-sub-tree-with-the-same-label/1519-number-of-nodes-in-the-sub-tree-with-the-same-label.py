class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        ans = [0] * n
        def go(index, parent):
            count = collections.Counter()
            
            for edge in graph[index]:
                if edge != parent:
                    count += go(edge, index)
            
            count[labels[index]] += 1
            ans[index] = count[labels[index]]
            return count
        
        go(0, -1)
        return ans