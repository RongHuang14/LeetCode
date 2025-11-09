#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         """
#         1. 排列型回溯
#         数组path记录路上的数
#         集合s记录剩余未选数字
#         """
#         n = len(nums)
#         ans = []
#         path = [0] * n
#         # i表示需要构造大于等于i的排列
#         # s表示剩余可以选的数的集合
#         # T: O(n! * n) n!个节点,每次n的浅拷贝
#         # S: O(N),浅拷贝
#         def dfs(i, s):
#             if i == n:
#                 ans.append(path.copy())
#                 return
#             for x in s:
#                 path[i] = x
#                 dfs(i + 1, s-{x})
#         dfs(0, set(nums))
#         return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        1. 排列型回溯
        用一个布尔数组onPath记录在path中的数字，如果nums[i]在path中，则onPath[i]为真
        """  
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            # 枚举下标
            for j in range(n):
                # 可以选
                if not on_path[j]:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False # 恢复现场
        dfs(0)
        return ans    

# @lc code=end

