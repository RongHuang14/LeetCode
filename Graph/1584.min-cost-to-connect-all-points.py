#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.cc = n
    
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
            self.size[root_x] += root_y
        return True
            
              
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        思路：Kruskal算法求最小生成树
        1. 将所有可能的边按曼哈顿距离排序
        2. 使用Union-Find检测环，贪心选择最小边
        3. 选择n-1条边连接n个点
        
        时间复杂度: O(n²log n) - 主要是排序
        空间复杂度: O(n²) - 存储所有边
        """
        # Step 1: 构建所有可能的边 (cost, point_i节点编号, point_j)
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                manhattan_dis = abs(points[i][0] - points[j][0]) + \
                    abs(points[i][1] - points[j][1])
                edges.append((manhattan_dis, i, j))
        edges.sort()
        
        # Step 2: Kruskal算法 - 贪心选择不成环的最小边
        uf = UnionFind(n)
        min_cost = 0
        edge_select = 0
        for cost, u, v in edges:
            if uf.union(u, v):
                min_cost += cost
                edge_select += 1
                
                # Prunning, exit the if go ahead
                if edge_select == n - 1:
                    break
        return min_cost
            
if __name__ == "__main__":
    sol = Solution()
    # test1
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]] # excepted: 20
    print(sol.minCostConnectPoints(points1))   
        
        
                
        
        
# @lc code=end

