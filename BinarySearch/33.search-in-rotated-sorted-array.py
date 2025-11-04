#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """这题相比34不是找>=和<=的第一个数变成找target了
        和34一样target可能不在数组中
        1. 什么时候nums[mid]在target及其右侧，染成蓝色
        1)if nums[mid] > nums[-1], mid在两段递增数组的左边这段
         target > nums[-1],两个都在左边这段
            nums[mid] >= target,说明mid在target及其右侧，染成蓝色
        2) if nums[mid] <= nums[-1], mid在一段递增的或者两段递增的右边这段
           target > nums[-1], target在两段递增的左边这段
            mid还是在target及其右侧，染成蓝色
        3) target和mid都在第二段，nums[mid] >= target
        """
        def is_blue(i):
            end = nums[-1]
            # i在左边这段
            if nums[i] > end:
                # 1）i在左边这段，target在左边这段并且i所在的值>= target
                return target > end and nums[i] >= target
            # i在右边这段
            else:
                # 2）target在左边这段
                # 3）target在右边这段，并且i所在值>= target
                return target > end or nums[i] >= target
        # [0, n-1] -> (-1, n)
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right
        
# @lc code=end

