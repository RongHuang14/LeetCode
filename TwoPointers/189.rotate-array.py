#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        根本想不到这个
        双指针 - 翻转重组（通过部分或整体翻转来重新排列元素），利用了翻转的对称性，翻转两次 = 恢复原样
        右旋k步 = 把后k个元素移到前面 
        = 翻转全部 + 翻转前k个 + 翻转后n-k个
        原始：[1,2,3,4,5], k=2
        目标：[4,5,1,2,3]  # 后2个移到前面
        1. 翻转整个数组
            后k个[4,5]现在在前面了，但顺序反了
            前n-k个[1,2,3]现在在后面了，但顺序也反了  
        2. 翻转前k个
        3. 翻转后n-k个
        对于 k≥n 的情况，可以转换成 0≤k<n 的情况，k = k% n
        每旋转n次（数组长度），就回到原点
        T: O(N)
        S: O(1)
        """
        # 注：请勿使用切片，会产生额外空间
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        k = k % n # k > n，旋转是循环的，旋转k次 = 旋转(k % n)次
        reverse(0, n - 1)
        reverse(0, k - 1) # 翻转前k个（索引0到k-1）
        reverse(k, n - 1) # 翻转后n-k个（索引k到n-1）
        
        
        
# @lc code=end

