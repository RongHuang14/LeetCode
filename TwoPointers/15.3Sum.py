"""
1. two pointer: o(n^2) o(1)
- Sort the array.
- Fix one element (`nums[i]`) and use two-pointer to find pairs summing to `-nums[i]`.
- Skip duplicates to avoid redundant triplets.
"""

class Solution:
    # [-4, -1, -1, 0, 1, 2]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # fix the first num
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two sum
            two_sums = self.twoSum(-nums[i], i + 1, nums)
            for pair in two_sums:
                res.append([nums[i]] + pair)
        return res

    # return the target tuple
    def twoSum(self, target, idx, nums):
        l, r = idx, len(nums) - 1
        tup = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                tup.append([nums[l], nums[r]])
                # remove duplicate
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
        return tup
    
'''
用这个写法要不总是犯错
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums) - 1 
        res = []
        for i in range(len(nums) - 2):
            # fix the first number
            # skip duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # start from i + 1, find two num sum == -nums[i]
            l, r = i + 1, len(nums) - 1 
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # find next two sum
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res