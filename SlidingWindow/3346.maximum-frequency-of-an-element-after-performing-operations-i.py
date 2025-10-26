#
# @lc app=leetcode id=3346 lang=python3
#
# [3346] Maximum Frequency of an Element After Performing Operations I
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        
        # 三指针：计算有多少数能变成nums[i]
        left = right = 0
        i = 0
        while i < n:
            x = nums[i]
            cnt = 0
            
            # 统计x出现的次数
            j = i
            while j < n and nums[j] == x:
                cnt += 1
                j += 1
            
            # 左指针：找到第一个 >= x-k 的位置
            while left < n and nums[left] < x - k:
                left += 1
            
            # 右指针：找到第一个 > x+k 的位置
            while right < n and nums[right] <= x + k:
                right += 1
            
            # [left, right)范围内的数都能变成x
            total_can_become_x = right - left
            ans = max(ans, min(total_can_become_x, cnt + numOperations))
            
            i = j
        
        # 如果已经达到最优，无需继续
        if ans >= numOperations:
            return ans
        
        # 双指针：考虑变成不在nums中的数
        left = 0
        for right in range(n):
            # 窗口[left, right]中的数都能变成某个相同的值
            # 这个值在[nums[right]-k, nums[left]+k]的交集中
            while nums[left] < nums[right] - 2 * k:
                left += 1
            ans = max(ans, min(right - left + 1, numOperations))
        
        return ans
        
# @lc code=end

