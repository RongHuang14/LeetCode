#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        T:O(N) S:O(1)
        """
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        p0 = dummy = ListNode(next=head)
        
        pre = None
        cur = p0.next
        while n >= k:
            n -= k
            # 每次进入这里，都要反转新的 k 个节点
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
        
# @lc code=end

