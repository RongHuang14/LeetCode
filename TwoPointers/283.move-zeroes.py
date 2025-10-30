#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        write read pointer, write in place
        1. write pointer go through all the elements, write to revise
        2. use r to read, i to read.
        a. nums[i] == 0, skip
        b. if nums[i] != 0: keep, put the ele on r
            nums[r] = nums[i]
            r += 1
        3. add 0 from r to the end of the array
        """
        r = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[r] = nums[i]
                r += 1
        
        for _ in range(r, len(nums)):
            nums[r] = 0
            r += 1
        
        
# @lc code=end

