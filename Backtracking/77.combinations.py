#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """从n个数中选出k个数的组合
        可以看成是长度固定的子集
        因此只要用子集型回溯的思路，然后倒序遍历当可以选的数不够时剪枝就行
        """
        ans = []
        path = []
        def dfs(i):
            d = k - len(path)
            if i < d:
                return                                                                                                     
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i, 0, - 1):
                path.append(j)
                dfs(j - 1)
                path.pop()
        dfs(n)
        return ans
# @lc code=end

