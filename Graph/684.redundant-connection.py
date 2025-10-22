#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
"""
1.union find: 
t:o(inverse ackerman function),nearly o(1)
s:o(1)
用Union find来判断是否需要添加冗余边，如果ai,bi不属于一个group,就可以add edge
如果属于一个group,就不可以add edge,否则会形成环，因此可以把这个edge remove
多条就return input 最后出现的那个

注意这里编号是1-N,所以Unionfind初始化传入n+1,整个idx往后偏1位，0号位置闲置
节点编号：1, 2, 3, 4, 5 (5个节点)
uf = UnionFind(6)  # 传入6（5+1）
parent = [0, 1, 2, 3, 4, 5]
          ↑  ↑  ↑  ↑  ↑  ↑
        浪费  1  2  3  4  5 (向右移动一位)
"""
from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: 
            return False   
        
        # union by size
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        for ai, bi in edges:
            # have the same root, then the edage can be removed
            if not uf.union(ai, bi):
                return [ai, bi]
        return []

if __name__ == "__main__":
    from typing import List
    
    s = Solution()
    
    # Test 1: Basic triangle
    edges1 = [[1,2],[1,3],[2,3]]
    print(s.findRedundantConnection(edges1))  # [2,3]
    
    # Test 2: More complex
    edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(s.findRedundantConnection(edges2))  # [1,4]
    
    # Edge case: Minimum size
    edges3 = [[1,2],[2,3],[3,1]]
    print(s.findRedundantConnection(edges3))  # [3,1]
# @lc code=end

