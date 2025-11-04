#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def lowerBound(row, target):
            # [0, n-1] -> (-1, n)
            left, right = -1, len(row)
            while left + 1 < right:
                mid = (left + right) // 2
                if row[mid] >= target:
                    right = mid
                else:
                    left = mid
            return right

        for row in matrix:
            right = lowerBound(row, target)
            if right == len(row) or row[right] != target:
                continue
            else:
                return True
        return False
# @lc code=end

