#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """双指针-原地修改
        a = [0,0,1,1,1,2,2,3,3,4]
        a0肯定要保留，从a1开始讨论：
        a. a1 = a0, a1是重复项，去掉
        b. a1 != a0, a1不是重复项，保留
        •	i 👉 当前正在扫描的元素
        •	k 👉 下一个“要保留的元素”要放入的位置
        一旦发现当前元素和前一个一样（nums[i] == nums[i - 1]），说明它是重复的，不需要保留，因此：
            •	我们不动 k；
            •	也不改 nums；
            •	直接跳过，让循环自动执行下一步，也就是 i 往前走。
            
        1. 初始化k = 1,指向下一个要存放"唯一元素"
        2. 从i = 1 开始遍历Nums
        3. 如果nums[i] = nums[i - 1],那么nums[i]是重复项，不保留,跳过k不变
        4. 如果nums[i] != nums[i - 1],那么nums[i]不是重复项，保留，就把它"搬运"到前面的位置 k
        填入nums[k]中，
        然后把k + 1
        5.  遍历结束后，k就是nums中唯一元素的数量，返回k
        """
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                k += 1
        return k
                
                
        
# @lc code=end

