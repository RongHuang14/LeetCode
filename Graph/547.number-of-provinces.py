#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            visited[i] = True
            for nei in range(n):
                if isConnected[i][nei] == 1 and not visited[nei]:
                    dfs(nei)

        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res
        
        
# @lc code=end

