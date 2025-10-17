"""
1. brute force: o(n^2)
iterate through the array with index i and compute
the product of the array except for that index element.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            res.append(product)
        return res

"""
2. division: O(n), case: without 0, 1's 0, 1 more 0
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        # non-zero product and zero-cnt
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        # zero_cnt > 1 all will be 0
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            # have 1 zero
            if zero_cnt == 1:
                res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
    
'''
Prefix & Suffix: use space to replace time  O(N) O(N) DP
break the problem, [1,2,3,4]
nums[2] = pref[2] * suff[2], which is 1 * 12 = 12
res[i] = pref[i] * suff[i]
First pass: Compute prefix array.
Second pass: Compute suffix array.
way to calculate prefix product and suffix product:
prefix[i](product from nums[0] to nums[i-1]) = prefix[i - 1] * nums[i - 1] (reuse prefix[i - 1], time o(n^2) -> o(n))
prefix[i](product from nums[i + 1] to nums[n - 1]) = suffix[i + 1] * nums[i + 1] (reuse suffix[i + 1], time o(n^2) -> o(n))

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff = [1] * n, [1] * n
        res = [1] * n
        # [1,2,4,6]
        # prefix_pro: [1,1,2,8]
        # suffix_pro: [48,24,6,1]
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
"""
Prefix & Suffix (Optimal) o(n) o(1) ✅
- First pass: Store prefix in res.
- Second pass: Multiply suffix in res.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # Compute prefix product in res
        prefix = 1
        for i in range(n):
            res[i] = prefix  # prefix_prod(excluding element)
            prefix *= nums[i]  # update prefix_prod

        # Compute suffix product in res
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix  # suffix_prod(excluding element)
            suffix *= nums[i]  # update suffix_prod
        return res