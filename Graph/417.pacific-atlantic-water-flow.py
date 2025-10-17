#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# """
# 1.DFS正向遍历，超时，时间复杂度是O(m×n×m×n)❌
# 1） 每个cell开始dfs,如果cell可以走到 heights[0][c] or heights[r][0]
# and cell可以走到heights[r][n-1] or heights[m-1][c],则符合要求
# 2） DFS,return true/fasle看是否能走到
# 每个cell上下左右开始dfs
# 递归参数：cell
# 递归边界：
#     能走到：r,c符合上面要求，return true
#     注意这里不能一个dfs同时记录两个状态，因为dfs是一条路走到底的，当你走到p的时候你不知道是否其他路径能到达A，
#     因此需要有两个bool值
#     不能走到：超出边界了，return fasel
# 递归关系：
#     上，下，左，右
#     if heights[r][c] >= heights[r]

# """
# # @lc code=start
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         m = len(heights)
#         n = len(heights[0])
#         directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
    
#         def dfs(r, c):
#             # 步骤1：我直接在边界吗？
#             can_pacific = (r == 0 or c == 0)
#             can_atlantic = (r == m-1 or c==n-1)
            
#             tmp = heights[r][c]
#             heights[r][c]= -1
            
#             # 步骤2：我虽然不在边界，但能通过邻居到达吗？
#             for dr, dc in directions:
#                 nr,nc = r+dr, c+dc
#                 # 检查边界、未访问、水能流过去
#                 if(0 <= nr < m and 0 <= nc < n) and heights[nr][nc] != -1 and heights[nr][nc] <= tmp:
#                     p, a = dfs(nr, nc)
#                     # 如果水能流到邻居，而邻居能到海洋，那当前位置也能到海洋
#                     can_atlantic = can_atlantic or dfs(nr, nc)
#                     can_pacific = can_pacific or dfs(nr, nc)
            
#             heights[r][c] = temp
#             return can_atlantic, can_pacific
        
#         res = []
#         for r in range(m):
#             for c in range(n):
#                 p, a = dfs(r, c)
#                 if p and a:
#                     res.append([r,c])
#         return res
"""
2. 反向DFS,应该反向思考从海洋边界触发，看能到达哪些cell（水往高处流）
从海洋边界问：我能到达哪些格子？
- 太平洋边界一次DFS → 找出所有能到达的格子
- 大西洋边界一次DFS → 找出所有能到达的格子
- 交集就是答案
DFS通过修改visited参数来收集结果，而不是通过return
visited既是"已访问标记，也是能到达节点啊
注意py里集合语法：
    & 交集
    | 并集
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m = len(heights)
        n = len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 在边界内，没有访问过，且水往高处流
                if (0<= nr < m and 0 <= nc < n and (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
                
        # 找出所有能从太平洋到达的点
        # 找出所有能从大西洋到达的点
        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n-1, atlantic)
        
        for c in range(n):
            dfs(0, c, pacific)  
            dfs(m-1,c, atlantic)    

        return list(pacific & atlantic)
        
# @lc code=end

