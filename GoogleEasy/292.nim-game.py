#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        Game Theory - Losing State Analysis (博弈论 - 必败态分析)
        
        游戏规则：
        - 两人轮流拿石头，我先手
        - 每次可以拿1-3块
        - 谁拿到最后一块谁赢
        - 双方都采用最优策略 (optimal strategy)
        
        核心发现：
        1. 面对4块石头必输（无论拿1/2/3，对手都能拿完剩余的）
        2. 面对8块石头必输（无论拿几块，对手都能调整让你面对4）
        3. 必败点 (losing positions)：4, 8, 12, 16... （4的倍数）
        
        算法思路：
        - 如果n是4的倍数：
          无论我拿x块(1≤x≤3)，对手拿(4-x)块
          每轮共拿4块，我总会面对4的倍数，最终面对4必输
        
        - 如果n不是4的倍数：
          我可以拿掉余数，让对手面对4的倍数
          对手陷入必败态 (losing state)，我必赢
        
        结论：n % 4 != 0 时我赢，否则我输
        
        时间复杂度：O(1)
        空间复杂度：O(1)
        """
        return n % 4 != 0
        
# @lc code=end

