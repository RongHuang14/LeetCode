#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
# T:O(n) S:O(1)
class Solution:
    def max_consec_one(self, nums, k):
        res = float("-inf")
        l = 0
        n = len(nums)
        count = 0 # count for 0

        # find a window:count for 0 < k
        for r in range(n):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            win_len = r - l + 1
            res = max(res, win_len)
        return res

if __name__ == "__main__":
    sol = Solution()
    # Test 1: Normal case
    nums1 = [1,1,1,0,0]
    print(sol.max_consec_one(nums1, 2)) # Expected: 5
    # Test 2: k = 0, can't flip
    nums2 = [1,0,1,1]
    print(sol.max_consec_one(nums2, 0)) # Expected: 2
    # Test 3: array are all 0
    nums3 = [0,0,0,0]
    print(sol.max_consec_one(nums3, 2)) # Expected: 2
# @lc code=end

