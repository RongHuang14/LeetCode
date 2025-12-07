#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        path = []
        
        def dfs(i: int) -> None:
            if i == n:
                res.append(path.copy())
                return
            # 选x
            x = nums[i]
            path.append(x)
            dfs(i + 1)
            path.pop() 
            
            # 不选 x，那么后面所有等于 x 的数都不选
            # 如果不跳过这些数，会导致「选 x 不选 x'」和「不选 x 选 x'」这两种情况都会加到 ans 中，这就重复了
            i += 1
            while i < n and nums[i] == x:
                i += 1
            # 这里的dfs(i)里面的i，已经不是“原来的那个i”，而是“跳过了一串等于x之后的下一个位置”
            # 所以它实际上是：dfs(第一个不等于x的下标)，和之前没有重复时的dfs(i + 1)不一样
            dfs(i)
            
        dfs(0)
        return res
            
        
# @lc code=end

