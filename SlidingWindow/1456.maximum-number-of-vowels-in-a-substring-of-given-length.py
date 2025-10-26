#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """滑动窗口
        1. 窗口定长k,枚举右端点r, 左端点index = r - k + 1
        2. 每次窗口变化的时候都更新窗口内元音字母个数，并且记录最大元音字母个数
        3. 遍历完后返回
        """
        ans = vowel = 0
        
        # 枚举窗口右端点 i
        for i, c in enumerate(s):
            # 1. 右端点进入窗口
            if c in "aeiou":
                vowel += 1
                
            left = i - k + 1 # 窗口左端点
            # 窗口大小不足 k，尚未形成第一个窗口
            if left < 0:
                continue
            
            # 2. 更新答案
            ans = max(ans, vowel)
            
            # 3. 左端点离开窗口，为下一个循环做准备
            if s[left] in "aeiou":
                vowel -= 1
        return ans
            
# @lc code=end

