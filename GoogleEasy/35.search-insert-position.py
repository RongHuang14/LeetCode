#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """binary search
        = fidn the first position >= target
        1.l, r = 0, len(nums) - 1
        2. target in array
        compare nums[mid] and target
        if nums[mid] < target, then target should be in right
        left = mid + 1
        otherwise, target should be in left
        right = mid - 1
        otehrwise, equal just return
        3. target not in array
        Loop Invariant:
        nums[0 .. left - 1] < target
        nums[right + 1 .. end] > target
        search in [left, right]
        if left > right, search space is empty, return
        when er exit the roop:
        left = right + 1
        the first elemnt greater then target is left
        
        T: O(logn)
        S: O(1)
        """
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left    
        
# @lc code=end

