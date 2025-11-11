#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """双指针，中心扩展
        O(n^2)
        O(1)
        """
        # helper function to return the currrent longes palindrome
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        for i in range(len(s)):
            # odd: 中心为 s[i]
            odd = expand(i,i)
            # even: 中心为s[i]和s[i + 1]
            even = expand(i, i + 1)
            res = max(res, odd, even, key=len)
        return res
            
        
# @lc code=end

