#
# @lc app=leetcode id=3461 lang=python3
#
# [3461] Check If Digits Are Equal in String After Operations I
#

# @lc code=start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """One pass, simulation
        T:O(N^2)
        S:O(1),这里不要创建新的s了，要不空间会是O(n)
        """
        a = [ord(c) - 48 for c in s]
        m = len(a)
        
        while m > 2:
            for i in range(m - 1):
                a[i] = (a[i] + a[i + 1]) % 10
            m -= 1
        return a[0] == a[1]

# 还有一种O(N)的解法，比较复杂欧拉定理 
# @lc code=end

