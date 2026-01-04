#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(res, cur_max)
        
        return res

if __name__ == "__main__":
    sol = Solution()
    # Normal case: all positive -> [2,3,4] = 24
    nums1 = [2, 3, 4]
    print(sol.maxProduct(nums1))
    # Normal case: positive and negative -> [2,3] = 6
    nums2 = [2, 3, -2, 4]
    print(sol.maxProduct(nums2))
    # Edge case: contains zero -> 0
    nums3 = [-2, 0, -1]
    print(sol.maxProduct(nums3))
        
# @lc code=end

