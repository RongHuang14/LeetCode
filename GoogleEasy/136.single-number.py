#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Bit Manipulation
        XOR特性：偶数次XOR会抵消，奇数次会留下
        concept:
        a. If we take XOR of zero and some bit, it will return that bit, a ^ 0 = a
        b. If we take XOR of two same bits, it will return 0, a ^ a = 0
        c. a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        T: O(n)
        S: O(1)
        """
        res = 0
        for num in nums:
            res ^= num
        return res
        
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         """iteration.
#         排序 + 迭代， 成对检查
#         相同的数字必然相邻成对出现
#         单独的数字要么夹在中间，要么在末尾
#         candidate 默认是最后一个
#         单独的在中间：循环中会找到并返回
#         单独的在末尾：循环正常结束，返回最后一个
#         T: O(nlogn)
#         S: O(1)
#         """
#         nums.sort()
        
#         # 情况1：在循环中找到
#         for i in range(0, len(nums) - 1, 2):
#             if nums[i] != nums[i + 1]:
#                 return nums[i]
        
#         # 情况2：循环结束，单独的在最后
#         return nums[-1]
        
# @lc code=end

