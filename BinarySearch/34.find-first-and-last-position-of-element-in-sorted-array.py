#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def lowerBound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Binary Search
        找>=的第一个数和<=的最后一个数
        T: O(logn)
        S: O(1)
        """
        start = self.lowerBound(nums, target)
        # 所有数都<target或者target在数组中根本不存在
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lowerBound(nums, target + 1) - 1
        return [start, end] 
        
# @lc code=end

