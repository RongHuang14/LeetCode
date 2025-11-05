#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        找两个有序数组的中位数 - 二分切割法
        
        核心思想：
        1. 中位数的本质是将所有元素分成相等的两部分，使得：
           - 左半部分的所有元素 <= 右半部分的所有元素
           - 左右两部分数量相等（或左边多1个）
        
        2. 不需要真正合并数组，只需要找到正确的切割位置：
           nums1: [... left1 | right1 ...]  在位置i切割
           nums2: [... left2 | right2 ...]  在位置j切割
           
           其中 j = (m+n+1)/2 - i （确保左边总共有一半元素）
        
        3. 切割正确的条件：
           - left1 <= right2 （nums1左边最大 <= nums2右边最小）
           - left2 <= right1 （nums2左边最大 <= nums1右边最小）
        
        4. 二分搜索过程：
           - 在较短数组上二分（避免j越界）
           - 如果left1 > right2：说明nums1切多了，往左调整
           - 如果left2 > right1：说明nums1切少了，往右调整
        
        5. 返回中位数：
           - 奇数个：返回左边最大值 max(left1, left2)
           - 偶数个：返回 (左边最大 + 右边最小) / 2
        
        时间复杂度：O(log(min(m,n)))
        空间复杂度：O(1)
        """
        m, n = len(nums1), len(nums2)

        # 确保在较短数组上二分，防止j越界
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
            
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i  # +1确保奇数时左边多一个

            # 获取切割点附近的4个关键值
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # 检查切割是否正确
            if left1 > right2:
                right = i - 1  # nums1切多了，往左
            elif left2 > right1:
                left = i + 1   # nums1切少了，往右
            else:
                # 切割正确，计算中位数
                if (m + n) % 2 != 0:
                    return max(left1, left2)  # 奇数：左边最大值
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

        
# @lc code=end

