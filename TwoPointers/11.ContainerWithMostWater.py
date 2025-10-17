"""
O(n) time and O(1) space,n is the size of the input array.
"""

"""
1. brute force: o(n^2) o(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                res = max(res, area)
        return res

"""
2. two pointers from both ends: o(n) o(1)
area = (j - i) * min(heights[i], heights[j])
In the formula, the amount of water depends only on the minimum height. 
Therefore, it is appropriate to replace the smaller height value to make the smaller more greater.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
