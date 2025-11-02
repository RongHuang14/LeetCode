#
# @lc app=leetcode id=3370 lang=python3
#
# [3370] Smallest Number With All Set Bits
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        返回 ≥n 且二进制全为 1 的最小整数。
        思路：计算 n 的二进制长度 m，那么答案的二进制长度至少是 m。由于长为 m 的全为 1 的二进制数 ≥n，满足要求，所以答案的二进制长度就是 m，所以答案为
        2^m - 1
        上式的意思是，把 1 左移 m，得到 10..0,m个0，减1，得到11...1,m个1
        bit_length() 是Python内置的整数方法，用来获取一个数的二进制表示需要的位数（不包括符号位）
        T:O(1)
        S:O(1)
        """
        return (1 << n.bit_length()) - 1
        
# @lc code=end

