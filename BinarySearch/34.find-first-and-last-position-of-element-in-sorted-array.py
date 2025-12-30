#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def lowerBound(self, nums, target):
        # (), [0, n-1] -> (-1, n)
        n = len(nums)
        left, right = -1, n
        while left + 1 < right:
            mid = (left + right) // 2
            # red
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.lower_bound(nums, target)
        # Edge case: target不存在
        # 1. target不在数组中，且所有数都小于target，first == len(nums)
        # 2. target不在数组中，但在数组范围内, first == idx(第一个>target的数)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        last = self.lower_bound(nums, target + 1) - 1
        return [first, last]

if __name__ == "__main__":
    sol = Solution()
    # Normal case
    nums = [2,2,3,3,4]
    target = 3
    print(sol.searchRange(nums, target))  # [2,3]
    
    # Edge case 1: target不存在
    nums = [5,7,7,8,8,10]
    target = 6
    print(sol.searchRange(nums, target))  # [-1,-1]
    
    # Edge case 2: 空数组
    nums = []
    target = 0
    print(sol.searchRange(nums, target))  # [-1,-1]
        
# @lc code=end

