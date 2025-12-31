#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, m = 0, len(flowerbed)
        while i < m:
            # 可以种花
            if ((i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0 and (i == m - 1 or flowerbed[i + 1] == 0)):
                n -= 1
                i += 2  # 下一个位置肯定不能种花，直接跳过
            else:
                i += 1
        return n <= 0
                


if __name__ == "__main__":
    sol = Solution()
    # normal case: can plant
    flowerbed1, n1 = [1, 0, 0, 0], 1
    print(sol.canPlaceFlowers(flowerbed1, n1)) # True

    # normal case: can't plant
    flowerbed2, n2 = [1, 0, 0, 0], 2
    print(sol.canPlaceFlowers(flowerbed2, n2)) # False
        
# @lc code=end

