#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. 滑动窗口
        每次都是接到一个没有重复元素的子串后面（这个是我们自己定义的循环不变量），因此这个重复元素一定来自于我们接入的字符
        用哈希表判断是否有重复元素,记录出现的次数。
        while循环从不满足条件到满足条件
        T: O(N)
        S: O(128)/O(1)/O(len(s)),因为S是consists of English letters, digits, symbols and spaces，
        相当于一个ASCII码
        """
        ans = 0
        cnt = Counter() # hashmap, chat : occurencers
        left = 0
        
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1 # 移除左边，左指针负责收缩，注意子串要是连续的
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

