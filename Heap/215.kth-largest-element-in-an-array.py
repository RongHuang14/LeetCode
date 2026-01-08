#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
"""1.Min Heap
"""
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

"""2.Quick Selection
"""

if __name__ == "__main__":
    sol = Solution()
    # normal case 1：without repeat
    nums1 = [3,2,1,4,5]
    k1 = 2
    print(sol.findKthLargest(nums1, k1)) # output:4
    # edge case 1: with repeat
# @lc code=end

