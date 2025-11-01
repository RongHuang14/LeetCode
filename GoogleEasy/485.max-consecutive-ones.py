#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        One pass, O(n) O(1)
        """
        ans = 0
        count = 0 # caclute 1
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans
        
# @lc code=end

