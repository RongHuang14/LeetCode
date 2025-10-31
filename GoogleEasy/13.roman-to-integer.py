#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """一次遍历
        1. 从左到右遍历，比较s[i]和s[i + 1]
        if values[s[i]] < values[s[i + 1]],并且是合法的减法对，sum = s[i + 1]-s[i]
        else: sum += values[s[i]]
        T: O(n)
        S: O(1)
        """
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        # 只需要找在不在，查找o(1)
        subtract_pairs = {"IV", "IX", "XL", "XC", "CD", "CM"}
        sum = 0
        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i + 1]] and s[i]+s[i+1] in subtract_pairs:
                sum -= values[s[i]]
            else:
                sum += values[s[i]]
        return sum + values[s[-1]]
        
        
# @lc code=end

