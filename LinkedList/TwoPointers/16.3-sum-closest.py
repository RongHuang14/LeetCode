#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """相向双指针，和3sum类似但是这里是返回最接近的
        思路和 15. 三数之和 类似，排序后，枚举 nums[i] 作为第一个数，那么问题变成找到另外两个数，使得这三个数的和与 target 最接近，这同样可以用双指针解决。

        设 s=nums[i]+nums[j]+nums[k]，为了判断 s 是不是与 target 最近的数，我们还需要用一个变量 minDiff 维护 ∣s−target∣ 的最小值。分类讨论：

        如果 s=target，那么答案就是 s，直接返回 s。
        如果 s>target，那么如果 s−target<minDiff，说明找到了一个与 target 更近的数，更新 minDiff 为 s−target，更新答案为 s。然后和三数之和一样，把 k 减一。
        否则 s<target，那么如果 target−s<minDiff，说明找到了一个与 target 更近的数，更新 minDiff 为 target−s，更新答案为 s。然后和三数之和一样，把 j 加一。
        """
        nums.sort()
        n = len(nums)
        min_diff = inf
        
        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue  # 优化三

            # 优化一
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            # 优化二
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                elif s > target:
                    if s - target < min_diff:
                        min_diff = s - target
                        ans = s
                    k -= 1
                else: # s < target
                    if target - s < min_diff:
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans
# @lc code=end

