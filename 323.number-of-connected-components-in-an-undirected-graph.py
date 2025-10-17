#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
"""
1.DFS:判断连通分量 
O(V + E),O(V + E)
"""
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build the graph
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
       
        
        visited = set()  
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count

        
# @lc code=end

