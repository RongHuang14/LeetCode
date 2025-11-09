#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         """
#         T: n^2 * n!
#         s: n
#         """
#         ans = []
#         col = [0] * n
        
#         # def valid(r, c):
#         #     # 枚举从0到n-1的所有行
#         #     for R in range(r):
#         #         C = col[R]
#         #         if r + c == R + C or r - c == R - C:
#         #             return False
#         #     return True
            
#         # r表示当前可以枚举的行号，s表示剩余可以枚举的列号
#         def dfs(r, s):
#             # 所有都枚举好了
#             if r == n:
#                 ans.append(['.'*c + 'Q'+'.'*(n-1-c) for c in col])
#                 return
#             # r < n可以继续枚举没有选的列好
#             for c in s:
#                 # 判断放了这个皇后后，有没有和其余的皇后互相攻击到
#                 if all(r+c != R+col[R] and r-c != R-col[R] for R in range(r)):
#                 # if valid(r, c):
#                     col[r] = c #放皇后
#                     dfs(r + 1, s-{c})
                    
#         dfs(0, set(range(n)))
#         return ans


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        判断该位置能否放皇后能否o(1)
        T: n * n!
        s: n
        """     
        ans = []
        col = [0] * n
        on_path = [False] * n
        m = 2*n - 1
        diga1 = [False] * m
        diga2 = [False] * m
        
        def dfs(r):
            if r == n:
                ans.append(['.'*c + 'Q'+'.'*(n-1-c) for c in col])
                return
            for c in range(n):
                if not on_path[c] and not diga1[r+c] and not diga2[r-c]:
                    col[r] = c #放皇后
                    on_path[c] = diga1[r+c] = diga2[r-c] = True
                    dfs(r + 1)
                    on_path[c] = diga1[r+c] = diga2[r-c] = False
        dfs(0)
        return ans

# @lc code=end

