#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#

# @lc code=start
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)

        for i, j in reservedSeats:
            if j in (2, 3, 4, 5):
                seats[i].add(0)  # left block
            if j in (4, 5, 6, 7):
                seats[i].add(1)  # middle block
            if j in (6, 7, 8, 9):
                seats[i].add(2)  # right block

        res = 2 * n  # each row can hold at most 2 families

        for blocks in seats.values():
            if len(blocks) == 3:
                res -= 2
            else:
                res -= 1

        return res
# @lc code=end

