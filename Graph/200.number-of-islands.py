#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
"""
网格图dfs
1. start from a cell in the grid
2. dfs:是否连通，没有返回值
递归参数：[i,j]
递归边界：不是1，走到网格边界
递归关系：标记访问，上下左右继续调用dfs
"""
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid),len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        res = 0
        
        def dfs(r, c):
            if not (0 <= r < m and 0<= c < n):
                return
            if grid[r][c] != "1":
                return
            
            grid[r][c] = '2'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
                    
        
        
# @lc code=end

