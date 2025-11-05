#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        双序列双指针
        题目要求：合并两个有序数组，使得最后数组非递减，并且说num1足够大，要求原地修改
        因此需要把nums2合并进nums1,结果非递减
        1. 用三个指针，p1,p2读指针分别指向两个数组，p写指针指向最后一个有效的要写的nums1位置
        2. 观察遍历顺序，nums1有空余位置（末尾是0），如果从前往后合并，需要频繁移动元素
        从后往前合并可以直接覆盖，因此就可以用双指针倒序遍历
        3. p1 = m - 1,nums1 的最后一个有效元素位置
           p2 = n - 1,nums2 的最后一个元素
           p = m + n - 1,nums1 的最后一个位置（放最大值）
           比较 nums1[p1] 和 nums2[p2]：
           谁大就放谁到 nums1[p]
           对应指针左移（p1/p2)
           p每次左移
        T: O(m + n)
        S: O(1)
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # nums2 还有要合并的元素
        while p2 >= 0:
            # 如果 p1 < 0，那么走 else 分支，把 nums2 合并到 nums1 中
            # 因为nums1已经处理完了
            # 放p1
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            #  放p2
            else:
                nums1[p] = nums2[p2]  # 填入 nums2[p1]
                p2 -= 1
            p -= 1
                
            
            
             
            
        
        
# @lc code=end

