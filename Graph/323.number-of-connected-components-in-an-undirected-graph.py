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
from typing import List
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
"""
2. Union Find
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n # 集合大小
        self.cc = n # 联通分量数量
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        self.cc -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u,v)
        return uf.cc
        
if __name__ == "__main__":
    sol = Solution()
    # normal case1: 
    print(f"Normal Case: {sol.countComponents(5, [[0,1], [1,2], [3,4]])}") # Output: 2

    # Edge Case 1: No edges (Every node is its own island)
    # Expected Output: 3
    print(f"No edges: {sol.countComponents(3, [])}") 

    # Edge Case 2: One long line (All nodes are connected)
    # Expected Output: 1
    print(f"Chain: {sol.countComponents(4, [[0,1], [1,2], [2,3]])}")


        
# @lc code=end

