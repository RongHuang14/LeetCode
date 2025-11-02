#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
from collections import Counter
from math import gcd
class Solution:
    """
    t divides s
    如果 s = t + t + ... + t（重复若干次），那就说 t 能整除 s。
    找出能同时整除两个字符串的最长公共子串
    Greatest Common Divisor
    1. 若 str1 + str2 != str2 + str1，说明两者不由同一基串构成，答案为 ""。
    2. x 的长度必须是能同时整除 len(str1) 和 len(str2) 的数
    len(str1) = len(x) * m  
    len(str2) = len(x) * n
    所以它的长度一定是 len(str1) 和 len(str2) 的 公约数
    而最大的可能长度，就是它们的 最大公约数 (gcd)。
    str1 = "ABABAB" → 长度 6  
    str2 = "ABAB"   → 长度 4
    gcd(6, 4) = 2
    math 模块自带这个函数，用法非常简单：
    from math import gcd
    print(gcd(6, 4))   # 输出 2
    
    """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2 + str1:
            return ""
        g = gcd(len(str1), len(str2))
        return str1[:g]
# @lc code=end

