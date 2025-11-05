#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        two pointer
        1. 题目说三元组顺序不重要，并且i,j,k不相等，可以相当于i<j<k
        2. 枚举i，转化成剩下两数之和 = -nums[i]
        3. 不可以包含重复的三元组，因此我们需要跳过相同元素进行去重，因此只要当前枚举的数与上一个数相同时，跳过重复的数即可
        去重这里先移动再比较当前这个和上一个，以及先比较当前这个和下一个再移动都行，注意是等于的时候去重哈，因为本质是希望不要收集到重复的结果
        但是！比较前一个更自然， 因为：第一个元素永远要处理（i=0时没有前一个）从第二个开始，如果和前面相同就跳过
        T: sort-nlogn, loop-n, two-pointer-n,因此总的时间复杂度是o(n^2)
        S: O(1)，这里排序不算的话
        """
        nums.sort()
        ans = []
        n = len(nums)
        # 后面还要留两个数给j和k
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            # 剪枝
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[n - 1] + nums[n - 2] < 0:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s > -x:
                    k -= 1
                elif s < -x:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
            
# class Solution:
#     # [-4, -1, -1, 0, 1, 2]
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         # fix the first num
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             # two sum
#             two_sums = self.twoSum(-nums[i], i + 1, nums)
#             for pair in two_sums:
#                 res.append([nums[i]] + pair)
#         return res

#     # return the target tuple
#     def twoSum(self, target, idx, nums):
#         l, r = idx, len(nums) - 1
#         tup = []
#         while l < r:
#             if nums[l] + nums[r] < target:
#                 l += 1
#             elif nums[l] + nums[r] > target:
#                 r -= 1
#             else:
#                 tup.append([nums[l], nums[r]])
#                 # remove duplicate
#                 while l < r and nums[l] == nums[l + 1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r - 1]:
#                     r -= 1
#                 l += 1
#                 r -= 1
#         return tup
        
# @lc code=end

