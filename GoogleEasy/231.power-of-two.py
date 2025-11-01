#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """迭代
        一次循环找规律
        2的幂 = 不断×2 → 反过来不断÷2
        不断除以2
        如果n是2的幂，那么不断除以2最终会得到1：
        ```
        16 → 8 → 4 → 2 → 1 ✓
        12 → 6 → 3 → ... ✗ (3不能被2整除)
        T: O(logn),每次除以2，n呈**指数级减少
        S: O(1)
        """
        if n <= 0 or (n % 2 != 0 and n != 1):
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Bit manupulation
        计算机就是用二进制的，2的幂在二进制中特别特殊：
        1  = 0001
        2  = 0010
        4  = 0100
        8  = 1000
        16 = 10000
        **发现规律**：2的幂只有**一个1**，其他都是0！
        如果n是2的幂，n & (n-1) = 0
        n-1会把n最右边的1变成0（二进制从右往左），该1右边的0全变成1
        例： n   = 8 = 1000
        n-1 = 7 = 0111  (最右边的1变0，右边的位全变1)
        1000
        & 0111
        ------
        0000  (结果是0！)
        例：n = 6（不是2的幂，二进制会有多个1，不能全都消掉，不会都变成0）
        n   = 6 = 0110
        n-1 = 5 = 0101

        0110
        & 0101
        ------
        0100  (不是0，因为6有多个1)
        
        T: O(1)
        S: O(1)
        """
        return n > 0 and n & (n - 1) == 0
# @lc code=end

