#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#

# @lc code=start
from typing import List
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        def func(x, a, b, c):
            return a * x * x + b * x + c

        if a > 0:
            # fill from right to end
            # for 循环保证了恰好执行 n 次，每次循环处理 1 个元素（移动 l 或 r)
            # n 次循环后，所有元素都被处理完,因此不用while l <= r
            for i in range(n - 1, -1, -1):
                x = func(nums[l], a, b, c)
                y = func(nums[r], a, b, c)
                if x > y:
                    res[i] = x
                    l += 1
                else:
                    res[i] = y
                    r -= 1
        else:
            # fill from left to end
            for i in range(n):
                x = func(nums[l], a, b, c)
                y = func(nums[r], a, b, c)
                if x < y:
                    res[i] = x
                    l += 1
                else:
                    res[i] = y
                    r -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # normal case1: have negative and positive, a > 0
    nums1,a1,b1,c1 = [-4,-2,2,4], 1, 3, 5
    print(sol.sortTransformedArray(nums1,a1,b1,c1)) # [3,9,15,33]
    # normal case2: a < 0
    nums2, a2, b2, c2 = [-4,-2,2,4], -1, 3, 5
    print(sol.sortTransformedArray(nums2, a2, b2, c2))  # [-23,-5,1,7]
    # edge case1: a = 0
    nums3, a3, b3, c3 = [1, 2, 3], 0, 2, 1
    print(sol.sortTransformedArray(nums3, a3, b3, c3))  # [3, 5, 7]
    
        
# @lc code=end

