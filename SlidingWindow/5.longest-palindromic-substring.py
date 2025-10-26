#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1. 滑动窗口
        每次都是接到一个没有重复元素的子串后面，因此这个重复元素一定来自于我们接入的字符
        用哈希表判断是否有重复元素,记录出现的次数。
        while循环从不满足条件到满足条件
        """
        ans = 0
        cnt = Counter() # hashmap, chat : occurencers
        left = 0
        
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[c] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        
        
# @lc code=end

