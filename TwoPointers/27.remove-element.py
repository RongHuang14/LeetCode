#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """读写指针 - 原地修改
        1. 读写指针，一个用来读，一个用来写
        2. 初始化写指针 r = 0, 遍历数组, i指针用来读
        a. 如果nums[i] == val, 不保留，跳过
        b. 如果nums[i] != val, 保留， 需要写入位置r
            因此 nums[r] = nums[i], r += 1
        3. 遍历完数组，r指向下一个要写入的有效元素，返回r即是我们需要的长度
        """
        if len(nums) == 0:
            return 0
        r = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[r] = nums[i]
                r += 1
        return r
        
# @lc code=end

