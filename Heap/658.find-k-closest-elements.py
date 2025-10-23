#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left, right = 0, len(arr) - 1

        # while right - left >= k:
        #     if abs(arr[left] - x) > abs(arr[right] - x):
        #         left += 1
        #     elif abs(arr[left] - x) < abs(arr[right] - x):
        #         right -= 1
        #     else:
        #         right -= 1
        # return arr[left: right + 1]
        
        # binary search
        # if x - arr[mid] > arr[mid + k] - x
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left : left + k]

               
# @lc code=end

