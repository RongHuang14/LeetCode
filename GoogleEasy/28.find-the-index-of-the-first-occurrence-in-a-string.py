#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        暴力匹配
        T: O(N * M)
        S: O(1)
        """
        m, n = len(haystack), len(needle)
        # 每个起点都尝试
        for i in range(m - n + 1):
            s1 = i
            s2 = 0
            while s2 < n and haystack[s1] == needle[s2]:
                s1 += 1
                s2 += 1
            if s2 == n:
                return i
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP: 字符串问题,利用前缀信息跳过一些字符
        T:O(m + n),构建部分匹配表：O(n),匹配过程：O(m)
        S:O(n)
        """

# @lc code=end

