#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """前后缀分解
        1.每一个视为一个宽度为1的桶，需要计算左边这块木板的高度和右边这块木板的高度，两个取最小值
        左边的高度取决于左边的最大高度，因为高于这个高度的水会流出，右边的同理取决于右边的最大高度
        第一种做法：需要两个额外的数组
        a. 第一个数组存储从最左边到第i个位置的最大高度,也就是前缀的最大值
        b. 第二个数组存储从最右边到第i个位置的最大高度，也就是后缀的最大值
        对于每个前缀最大值，用上一个前缀最大值和当前高度取最大值，得到当前最大值
        后缀最大值同理，只不过从右往前算
        c. 同时遍历高度h,前缀最大值数组pre_max和后缀最大值数组suf_max,木板的高度和右边这块木板的高度，两个取最小值
        - 高度h[i],累加

            •前缀数组（prefix array）：
        从左往右计算、存的是“左边到当前位置的某种累积或极值”。
        👉 遍历方向：0 → n-1
            •后缀数组（suffix array）：
        从右往左计算、存的是“右边到当前位置的某种累积或极值”。
        👉 遍历方向：n-1 → 0
        T: O(N)
        S: O(N)
        """
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0] # 这里要用到 pre_max[i-1]，所以不能从 i=0 开始，初始化一下
        for i in range(1,n):
            pre_max[i] = max(pre_max[i - 1],height[i])
        
        suff_max = [0] * n
        suff_max[-1] = height[-1] # 同理
        for i in range(n - 2, -1, -1):
            suff_max[i] = max(suff_max[i + 1], height[i])
        
        ans = 0
        for h, pre, suff in zip(height, pre_max, suff_max):
            ans += min(pre, suff) - h # pre是从左到当前位置的最大值，一定 ≥ 当前的 height[i],suff同理因此不会出现负数
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        """相向双指针
        如果前缀最大值比后缀最大值小，那么左边木桶的容量就是前缀最大值，然后向右扩展
        反之，如果后缀最大值比前缀最大值小，那么右边木桶的容量就是后缀最大值，然后向左扩展
        1. L = 0, R = n-1 ,模拟这个过程
        T: O(N),每次移动O(1),指针移动的距离之和是O(N)
        S: O(1)
        """
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        pre_max = 0 # 前缀最大值用变量表示，一边移动指针，一边更新它的最大值
        suff_max = 0 # 后缀最大值同理
        
        # 左右指针还没相遇，注意这里是<=,因为相等时还可以计算相等位置的接水容量
        while left <= right:
            pre_max = max(pre_max, height[left])
            suff_max = max(suff_max, height[right])
            
            if pre_max < suff_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suff_max - height[right]
                right -= 1
        return ans
        
        
# @lc code=end

