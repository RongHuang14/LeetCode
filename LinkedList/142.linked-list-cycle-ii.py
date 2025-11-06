#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """快慢指针
        T:O(N),慢指针相遇前后都走了n步
        S:O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                # 让 slow 回到起点，fast 留在相遇点, 最终会在入口处相遇
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
# @lc code=end

