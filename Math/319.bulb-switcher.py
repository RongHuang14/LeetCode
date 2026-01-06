#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
        
if __name__ == "__main__":
    sol = Solution()
    n1 = 3
    print(sol.bulbSwitch(n1)) # 1
        
# @lc code=end

