#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. Recursion One
        # # edge case
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # if n == 0:
        #     return 1.0
        # half = self.myPow(x, n//2)
        # if n % 2 == 0:
        #     return half * half
        # else:
        #     return half * half * x
        
        # 2. Recursion
        res = 1
        if n == 0:
            return 1.0
        if n < 0: # x^-n = (1/x)^n
            x = 1 / x
            n = -n
        while n > 0:
            if n % 2 == 1:    # n是奇数
                res *= x
            x *= x            # 每次都平方x
            n //= 2           # 每次都减半n
        return res

            

if __name__ == "__main__":
    sol = Solution()
    # Normal case
    print(sol.myPow(2.0, 10))  # Expected: 1024.0
    # Edge case 1: negative exponent
    print(sol.myPow(2.0, -2))  # Expected: 0.25
    # Edge case 2: n = 0
    print(sol.myPow(5.0, 0))   # Expected: 1.0
        
# @lc code=end

