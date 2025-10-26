#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        1. 滑动窗口
        这里while条件是从不满足条件到满足条件
        l , r:以r为右端点的子数组的格式，此时右端点是固定的
        如果[l,r]的乘积是<k的，那[l+1,r]...[r,r]也是小于k的
        因此以r为右端点符合条件的个数为r-l+1，这里要不要+1可以代入边界情况，l == r
        """
        if k <= 1:
            return 0
        res = 0
        prod = 1
        left = 0
        for right, x in enumerate(nums):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        return res
            
                
            
        
# @lc code=end

