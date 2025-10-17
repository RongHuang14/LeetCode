"""
有点问题开闭区间
Binary Search:[) O(log n) O(1)
二分这个还是要多做几题，开闭区间还是要理解清楚，然后还有
找左边界模版和右边界模版和返回值的问题（就是找找第一个≥x的元素和最后一个≤x的元素）

Core idea:
Since the array is rotated and consists of two sorted segments,
we need to first determine which sorted segment mid is in.
Then, check whether target lies in that sorted range:
- If yes: perform normal binary search within that segment
- If no: discard that segment and continue searching

Steps:
1. Binary search with [l, r)
2. At each step:
   - If nums[mid] == target → return mid
   - If nums[mid] >= nums[l], then [l, mid] is sorted:
       - If target in [nums[l], nums[mid]) → r = mid
       - Else → l = mid + 1
   - Else, [mid, r) is sorted:
       - If target in (nums[mid], nums[r - 1]] → l = mid + 1
       - Else → r = mid
3. Return -1 if not found

Time: O(log n)
Space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) # 左闭右开：[l, r)
        while l < r:
            mid = (l + r) // 2
            # mid is in the left part
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            # mid is in the right part
            else:
                if nums[mid] < target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid
        return -1

# 闭区间写法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1# 左闭右开：[l, r)
        while left <= right:
            mid = (left + right) // 2
            # 直接找到目标值
            if nums[mid] == target:
                return mid
            # [left, mid) 是有序段（第一段的部分）
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:  # target在有序区间内
                    right = mid - 1
                else:
                    left = mid + 1   
            # (mid, right] 是有序段（第二段的部分）
            else:
                if nums[mid] < target <= nums[right]:  # target在有序右侧区间内
                    left = mid + 1
                else:  # target在左侧（包含旋转点）
                    right = mid - 1
        return -1
