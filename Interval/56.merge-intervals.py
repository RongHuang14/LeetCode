#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并重叠区间
        
        算法思路：
        1. 排序：按起点升序排序，保证后面的区间不会出现在前面区间的左边
        2. 贪心合并：维护结果数组，其最后一个元素是"当前正在合并的区间"
           - 如果新区间的起点 <= 当前区间的终点：可以合并，更新终点
           - 否则：不重叠，将新区间作为新的合并区间加入答案
        
        示例：[1,3],[2,6],[8,10],[15,18]
        - [1,3] 加入答案
        - [2,6]: 2<=3，合并为[1,6]
        - [8,10]: 8>6，不能合并，新区间加入答案
        - [15,18]: 15>10，不能合并，新区间加入答案
        结果：[[1,6],[8,10],[15,18]]
        
        时间复杂度：O(nlogn) - 排序
        空间复杂度：O(n) - 存储结果
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        ans = []
        for interval in intervals:
            if ans and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1]) # 更新右端点最大值
            else: # 不相交，无法合并
                ans.append(interval) # 新的合并区间
        return ans
        
        
# @lc code=end

