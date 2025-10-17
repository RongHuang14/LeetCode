"""
有点问题开闭区间
Binary Search to find the minimum in a rotated sorted array (no duplicates).
[)
- A rotated sorted array consists of two sorted segments.
  For example: [4, 5, 6, 1, 2, 3] → [4,5,6] and [1,2,3]
  The minimum is the first element of the second segment.

- Key idea: compare nums[mid] with nums[r], to check min is located in which segment
    - If nums[mid] > nums[r], mid is in the left segment → min must be in right
    - If nums[mid] < nums[r], mid is in the right segment → min could be mid or on the left

- Optimization: if current segment [l, r] is already sorted (nums[l] < nums[r]),
  then nums[l] is the minimum.

Time: O(log n)
Space: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]  # current segment already sorted

            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1  # min is in right segment
            else:
                r = mid      # min is in left segment (or mid)
        return nums[l]