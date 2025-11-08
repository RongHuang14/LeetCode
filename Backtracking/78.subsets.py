#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        1.回溯，从输入的角度思考
        T:O(2^N) * N, 只有选和不选两种选择，总共会递归2^N次，有这么多选择，每次选择copy的时间是o(N)
        S:O(N)
        """
        ans = []
        path = []
        n = len(nums)
        
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            dfs(i + 1)
            
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
        dfs(0)
        return ans
            
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        2.回溯，从答案的角度思考
        T:O(2^N) * N, 只有选和不选两种选择，总共会递归2^N次，有这么多选择，每次选择copy的时间是o(N)
        S:O(N)
        """
        ans = []
        path = []
        n = len(nums)
        
        def dfs(i):
            ans.append(path.copy())
            if i == n:
                return
            
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans
                 
# @lc code=end

