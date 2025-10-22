#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
"""
网格图dfs
1. 遍历每个格子，如果是未访问的陆地就是一个新的岛屿，因此这里可以将未访问的陆地进行标记区分访问与未访问
已访问标记为'2'，再对每一个cell为'1'的格子开始dfs,dfs完结束这个新的岛屿就被标记了，计数+1
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

