#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        # i:起始索引, s:剩余目标和
        def dfs(i, s):
            if s == 0:
                ans.append(path.copy())
                return
            if i == len(candidates) or s < 0:
                return 
            # select
            path.append(candidates[i])
            dfs(i, s - candidates[i])
            path.pop()
            
            # no selcet
            dfs(i + 1, s)
        dfs(0, target)
        return ans
# @lc code=end

