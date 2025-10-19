#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
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

