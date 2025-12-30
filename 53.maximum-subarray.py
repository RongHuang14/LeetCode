#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
"""
1. 前缀和 + 贪心
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = cur_sub = nums[0]
        for i in range(1, len(nums)):
            cur_sub = max(nums[i], cur_sub + nums[i])  # ← 选择更大的
            max_sub = max(max_sub, cur_sub)
        
        return max_sub

if __name__ == "__main__":
    sol = Solution()
    
    # Normal: 正负混合
    nums1 = [-1,2,3]
    print(sol.maxSubArray(nums1))  # 5
    
    # Edge 1: 全负数
    nums2 = [-2,-1]
    print(sol.maxSubArray(nums2))  # -1
    
    # Edge 2: 全正数
    nums3 = [1,2,3]
    print(sol.maxSubArray(nums3))  # 6
        
# @lc code=end

