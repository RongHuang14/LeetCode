#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        快慢指针找重复数（Floyd's Tortoise and Hare）
        
        关键洞察：
        1. n+1个数，范围[1,n]，由鸽巢原理必有重复
        2. 把数组看成链表：索引i的next是nums[i]
        3. 从索引0出发，永远不会回到0（值域是1-n）
        4. 重复数字造成多个索引指向同一位置，形成环
        
        转换思路：
        - nums = [1,3,4,2,2]
        - 0→1→3→2→4→2（循环）
        - 索引2是环入口，因为nums[3]=2和nums[4]=2都指向它
        - 这正是因为2是重复数字！
        
        算法步骤：
        1. 快慢指针找相遇点（快2步，慢1步）
        2. 一个指针回起点，都以速度1前进
        3. 相遇处就是环入口（重复数字）
        
        为什么一定有环：
        - n+1个位置跳转，只有n个目标
        - 从0出发永不回0，必然重复
        
        时间：O(n) - 最多遍历2n次
        空间：O(1) - 只用两个指针，不修改原数组
        """
        # 阶段1：找相遇点（就像链表找环）
        slow, fast = 0, 0 # 都从索引0开始
        while True:
            slow = nums[slow] # 走一步
            fast = nums[nums[fast]] # 走两步
            if slow == fast:
                break
        
        # 阶段2：找环入口（就是重复数字）
        slow = 0 # 一个回到起点
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
        
# @lc code=end

