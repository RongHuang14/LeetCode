#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:  # 注意是 >=
                right = mid  # 蓝色：>= target
            else:
                left = mid   # 红色：< target
        
        if right == len(nums) or nums[right] != target:
            return -1
        return right
# @lc code=end

