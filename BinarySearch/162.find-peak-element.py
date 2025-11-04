#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Binary Search
        T: O(logn)
        S: O(1)
        """
        # [0, n - 2] -> (-1, n - 1)
        left = -1 
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: # 蓝色
                right = mid
            else:
                left = mid
        return right
# @lc code=end

