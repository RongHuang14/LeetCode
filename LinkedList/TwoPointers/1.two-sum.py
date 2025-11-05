#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comple_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in comple_dict:
                return [i, comple_dict[complement]]
            comple_dict[num] = i
        return [-1, -1]
        
# @lc code=end

