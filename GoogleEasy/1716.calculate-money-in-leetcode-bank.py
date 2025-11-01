#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        """
        第1周：1, 2, 3, 4, 5, 6, 7  (周一开始是1)= 28
        第2周：2, 3, 4, 5, 6, 7, 8  (周一开始是2)= 35 (28+7)
        第3周：3, 4, 5, 6, 7, 8, 9  (周一开始是3)= 42 (35+7)
        每周比上周多7块！
                
        i
        
        """

        
# @lc code=end

