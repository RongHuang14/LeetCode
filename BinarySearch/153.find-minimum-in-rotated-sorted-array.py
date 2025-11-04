#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """二分
        最后一个数要么是最小值，要么在最小值右侧
        红色表示False:即最小值左侧
        蓝色表示true:即最小值及右侧
        根据这一定义，n-1必定是蓝色，[0, n-2]中二分
        1. nums[mid] < nums[-1]:
        nums[mid]要么是最小值，要么在最小值右侧,染成蓝色
        2. nums[mid] > nums[-1]:
        nums[mid]一定在最小值左侧，染成红色
        """
        # [0, n-2]
        # (-1, n-1)
        left, right = -1, len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid # 蓝色
            else:
                left = mid # 红色
        return right
# @lc code=end

