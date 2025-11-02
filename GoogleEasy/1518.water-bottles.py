#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """追踪剩余的空瓶子
        1. 维护当前的空瓶总数
        2. 每次兑换要记录：
        换了几瓶新水（空瓶 // numExchange）
        剩余几个空瓶（空瓶 % numExchange）
        3. 新的空瓶总数 = 剩余空瓶 + 刚喝完的新瓶
        T: O(logn)每次循环空瓶数量都在指数级减少,n = n // k,每次减少为原来的1/k → O(log n)
        S: O(1)
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            # 兑换
            exchanged = empty // numExchange
            remain = empty % numExchange
            
            # 喝掉新水
            total += exchanged
            
            # 更新空瓶数：剩余的 + 刚喝完的
            empty = remain + exchanged
        
        return total
        
# @lc code=end

