#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
"""
1. dfs + 边数检查：
只要连通 + 无环即可，连通 + n个节点的无向图有n-1条边肯定是无环，即树（仅对无向图成立）
连通，即dfs遍历完了发现visited节点数 == n说明每个节点都被访问过了
"""
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        dfs(0)
        return len(visited) == n
# @lc code=end

