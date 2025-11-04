#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            hours = sum(math.ceil(p / k) for p in piles)
            return hours <= h
        
        # [1, max(piles)], (0, max(piles) + 1)
        left, right = 0, max(piles) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid
        return right
# @lc code=end

