#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            # "如果开始时间小于上一个结束，说明重叠"
            if intervals[i][0] < prev_end:
                cnt += 1 # "删除当前（因为它结束更晚）"
            else: 
                prev_end = intervals[i][1] # "保留并更新"
        return cnt
        
        
# @lc code=end

