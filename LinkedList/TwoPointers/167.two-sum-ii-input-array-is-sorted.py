#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        把数组中的最小和最大相加与target进行对比，就知道了数组中所有Pair与target的关系了
        花费o(1)的时间知道o(n)的信息，因此能将o(N^2)优化到o(N),前提是数组是有序的
        T: O(N)
        S: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            elif s > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1] # 1-idex
# @lc code=end

