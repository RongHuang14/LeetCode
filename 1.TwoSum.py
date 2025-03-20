"""
1. brute force:  check every pair of numbers o(n^2) o(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""
2. hashmap: o(n) o(n) ✅
    - Check `diff` first to return the smaller index first.
    - Only return when `diff` is already in `seen`, ensuring `seen[diff]` comes before `i`.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val -> idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []