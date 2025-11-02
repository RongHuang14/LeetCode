#
# @lc app=leetcode id=3349 lang=python3
#
# [3349] Adjacent Increasing Subarrays Detection I
#

# @lc code=start
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """双指针分组循环
        找递增段，然后看能否凑出两个相邻的长度k的子数组
        T: O(N)
        S: O(1)
        """
        prev_segment_len = 0 # 上一个递增段的长度
        curr_segment_len = 1 # 当前递增段的长度
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # 在同一个递增段中
                curr_segment_len += 1
            else:
                # 段结束，检查！
                
                # # 可能1：当前段够长
                if curr_segment_len >= 2 * k:
                    return True
                
                # 可能2：前后两段配合？
                if prev_segment_len >= k and curr_segment_len >= k:
                    return True
                
                # 准备处理下一段
                prev_segment_len = curr_segment_len
                curr_segment_len = 1
                
        # 处理最后一段（它没有在else里被检查）
        # nums = [1, 2, 5, 6, 7, 8, 9]  k=2
        if curr_segment_len >= 2 * k:
            return True
        if prev_segment_len >= k and curr_segment_len >= k:
            return True
        
        return False
                
                
        
# @lc code=end

