#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache
        def dfs(i, j):
            if i < 0:
                return j + 1 # 插入剩余j+1个字符
            if j < 0:
                return i + 1 # 删除多余i+1个字符
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i, j-1), dfs(i-1,j), dfs(i-1,j-1)) + 1
        return dfs(n-1,m-1)
        
# @lc code=end

