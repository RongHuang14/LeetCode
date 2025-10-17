"""
O(n) time and O(1) space
"""


"""
1.brute force: o(n^2) o(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])
        return profit
"""
2.dp: dynamically maintaining the minimum buy-in price.o(n) o(1)✅
minPrice: prices[i] 左侧元素的最小值，表示遍历到第 i 天时，前 i 天中的最低买入价
profit: 表示前 i 天能获得的最大利润
由于只能买卖一次，所以在遍历中，维护 prices[i]−minPrice 的最大值就是答案
更新前 i 天的最高利润 profit ，即选择「前 i−1 天最高利润 profit 」和「第 i 天卖出的最高利润 price - min_price 」中的最大值
这就相当于f(n) = max(f(n-1), Xn)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit
