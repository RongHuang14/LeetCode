#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 还是从N个数中选k个数的组合，加一个判断这里也可以不加，然后剪枝即可
        # T: O(c(9,k) * k)
        # S: O(k)
        ans = []
        path = []
        def dfs(i, t):
            d = k - len(path)
            if t < 0 or t > (2 * i - d + 1) * d // 2:
                return
            if i < d:
                return                                                                                                    
            if len(path) == k:
                # 注意这里不需要判断t是否等于0，因为t==0时d=0, if t < 0 or t >0不成立，t只有等于0这一种情况
                ans.append(path.copy())
                return
            for j in range(i, 0, - 1):
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()
        dfs(9,n)
        return ans
# @lc code=end

