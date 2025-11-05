#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        T:O(N) S:O(1)
        """
        p0 = dummy = ListNode(next=head)
        
        # 循环了left - 1次
        for _ in range(left - 1):
            p0 = p0.next
        
        pre = None
        cur = p0.next
        # right - left + 1个元素
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre
        return dummy.next
        
        
# @lc code=end

