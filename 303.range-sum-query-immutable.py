#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
"""Prefix Sum
T: 时间复杂度：初始化是 O(n)，其中 n 是 nums 的长度。sumRange 是 O(1)。
S: O(n)
"""
class NumArray:

    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1) # 局部变量
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s # 把 s 保存为实例属性！

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

