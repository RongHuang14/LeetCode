#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """one pass, 原地修改
        T:O(N)
        S:O(1)
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
        
        
# @lc code=end

