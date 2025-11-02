#
# @lc app=leetcode id=3354 lang=python3
#
# [3354] Make Array Elements Equal to Zero
#

# @lc code=start
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """Simulation
        T:O(n²·m),遍历找所有0的位置 → O(n),每个0的位置：模拟2次（两个方向）,每次模拟：
        最坏情况要遍历整个数组多次
        每个非0元素最多被访问m次（m是数组元素的最大值）
        模拟过程：O(n·m)
        S:O(n),每次模拟创建数组副本：O(n)
        """
        # One simulation
        def simulate(nums, cur, dir):
            while 0 <= cur < len(nums):
                if nums[cur] == 0:
                    cur += dir
                else:
                    nums[cur] -= 1
                    dir = -dir
                    cur += dir
            return sum(nums) == 0
        
        count = 0
        # find all start
        for i in range(len(nums)):
            if nums[i] == 0:
                # go to left
                if simulate(nums[:], i, 1):
                    count += 1
                if simulate(nums[:], i, -1):
                    count += 1
        return count

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """前后缀分解
        计算出每个位置为0的砖块的前缀和后缀砖块数，注意初始方向也很重要
        1 0 2 start 3
        1 0 2 0 2
        a.左右两边砖块差值为1，只能向左走
        b.左右两块砖块一样，两边都行
        T: O(N)
        """
        suf = sum(nums) # 位置i**右边**所有数的和（不包括i本身）
        ans = pre = 0 # 位置i**左边**所有数的和
        for x in nums:
            if x:
                suf -= x # 从后缀中移除
                pre += x # 加入前缀
            elif pre == suf:
                ans += 2
            elif abs(pre - suf) == 1:
                ans += 1
        return ans
        
        
# @lc code=end

