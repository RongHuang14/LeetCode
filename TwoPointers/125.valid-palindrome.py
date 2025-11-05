#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """相向双指针
        1. l,r指向头和尾，移除所有non-aplphanumeric并且upper to lower然后一个个compare
        """
        left, right = 0, len
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].islower() != s[right].islower():
                return False
            left += 1
            right -= 1
        return True
                
# @lc code=end

