#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针
        1. 初始化最左和最右，min(最左，最右)和中间的线比较，中间的线比它短，面积不会比它大
        比它长/一样长也不会，因为面积是取决与短的线的，因此肯定不能选这个min这条线如果要更大的话，这样就排除了一个答案
        2. 哪条线短，移动哪条即去掉哪条，一样长移动哪个都行。移动之前先把面积算出来，如果比答案大就更新答案
        因为每次花O(1)的时间就去掉了一条线，因此算法的时间复杂度是o(n)
        宽度是索引的差值，而不是元素数量
        """
        ans = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[right], height[left])
            ans = max(area, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
            
        
# @lc code=end

