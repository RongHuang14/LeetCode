"""
1. brute force:  check every pair of numbers o(n^2) o(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""
2. hashmap: o(n) o(n) ✅
    - Check `diff` first to return the smaller index first.
    - Only return when `diff` is already in `seen`, ensuring `seen[diff]` comes before `i`.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val -> idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []

# notice:
# 	•	你要找的是「有没有一个数 + 当前数 = target」
# 	•	那这个「另一个数」必须在你当前之前就出现过
# 	•	所以一定是：
# 	•	先查配对数 diff 有没有出现过
# 	•	再把当前数放进字典供后面用
 
# 关于「先查 diff 还是先填充 dict」：

# 这取决于题目有没有自己和自己配对的情况：
# 	•	先查后存：适用于不允许自己和自己配对（即不能用同一个数两次）
# 	•	先存后查：适用于可以重复使用当前元素（比如找 all pairs）