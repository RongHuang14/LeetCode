#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        双指针-原地修改（分区交换，荷兰国旗问题）
        1. 三指针
        low: 0区的下一个位置
        mid: 当前正在处理的位置
        high: 2区的前一个位置
        分别初始化为0,0, n-1
        2. 处理逻辑：
        当arr[mid] == 0时，把它与 arr[low] 交换low += 1，mid += 1
        当 arr[mid] == 1：直接跳过，mid += 1
        当 arr[mid] == 2：把它与 arr[high] 交换，high -= 1（注意 
        mid不动，因为交换过来的值可能还需要判断
        low过来的一定是0或1（已经处理过的）
        high位置来的可能是0、1、2（未处理过的）
        low，mid已经处理过了因为已经先扫过了，high没有处理过
        [0, low) - 0, [low, mid) - 1, [mid, high] - 2
        [mid, high]是未处理区域，因此while mid <= high时继续处理
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
                
            
        
# @lc code=end

