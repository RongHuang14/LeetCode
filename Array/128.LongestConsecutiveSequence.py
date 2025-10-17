"""
1. Brute Force: O(n^2) O(1)
- For each num, count the longest sequence starting from it.
- Check existence of (num + 1), (num + 2), ... in nums.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res= 0
        for num in nums:
            length = 1
            current = num
            while current + 1 in nums:  # O(n) check
                current += 1
                length += 1
            res = max(res,length)

        return res

"""
2. Sorting: O(n log n) time, O(1) space
- Sort nums to align consecutive numbers.
- Iterate through sorted nums, checking `nums[i] == nums[i-1] + 1`.
- If consecutive, extend `streak`, else reset it.
- Track the longest `streak` found.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res, streak = 1, 1  # At least one number means streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            elif nums[i] == nums[i - 1] + 1:  # Consecutive number
                streak += 1
            else:  # Reset streak
                res = max(res, streak)
                streak = 1

        return max(res, streak)  # Ensure last streak is counted

"""
3. hash set optimized: O(n) time, O(1) space.
暴力解每个num都作为start,并且重复检查num+1...n, hash set优化仅检查可能的seq start
每个element最多访问两次，时间复杂度o(n)
- Use a HashSet for remove duplication andO(1) lookups.
- Only start counting from `num` if `num - 1` is not in the set (ensures it's a sequence start).
- Expand the sequence by checking `num + 1, num + 2, ...` in the set.
- Track the longest sequence found.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
