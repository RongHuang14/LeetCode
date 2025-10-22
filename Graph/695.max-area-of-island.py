#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid),len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        res = 0
        
        # 返回这个岛屿的面积
        def dfs(r, c):
            nonlocal area
            if not (0 <= r < m and 0<= c < n):
                return 0
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2
            area += 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        
        for i in range(m):
            for j in range(n):
                # 找到一个新的岛屿
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    res = max(res, area)
        return res
# @lc code=end

