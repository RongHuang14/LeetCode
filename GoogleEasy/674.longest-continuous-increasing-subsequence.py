#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """one pass 
        T: O(n)
        S: O(1)
        """
        if not nums:
            return 0
        ans = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                cur_len = 1
            ans = max(ans, cur_len)
        return ans
        
# @lc code=end

