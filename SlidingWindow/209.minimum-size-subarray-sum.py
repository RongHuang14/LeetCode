#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        滑动窗口
        left移动指针时，子数组的和不断变小，while从满足条件要求不断地变，
        变成不满足条件要求，窗口内是有单调性的，只有满足了单调性我们才可以使用双指针
        当然while条件还可以从不满足条件变成满足条件
        T: O(N),left从0到n, right从0到n, 2n次
        S: O(1)
        """
        n = len(nums)
        left = 0
        s = 0
        res = float("inf")
         
        # x: nums[right]
        for right, x in enumerate(nums):
            s += x
            # # shrink: to find optimal solution,满足条件缩小到直到不满足条件
            # # 这里不用写while left <= right,是这个条件已经满足了
            # while s - nums[left] >= target:
            #     s -= nums[left]
            #     left += 1
            
            # if s >= target:
            #     res = min(res, right - left + 1)
            while s >= target:
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1
        return res if res < float('inf') else 0
            
                
            
            
        
# @lc code=end

