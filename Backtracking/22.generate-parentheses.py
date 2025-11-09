#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """组合问题
        T: O(N) * C(2N,N),由于左右括号之间实际会有限制,Catalan number
        S: O(N)
        """
        m = n * 2
        ans = []
        path = [''] * m
        
        def dfs(i, open):
            if i == m:
                ans.append("".join(path))
                return
            if open < n:
                path[i] = '('
                dfs(i + 1, open + 1)
            if i - open < open:
                path[i] = ')'
                dfs(i + 1, open)
        dfs(0,0)
        return ans
        
# @lc code=end

