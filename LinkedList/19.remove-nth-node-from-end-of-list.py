#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Step 1：right 先走 n 步
        right 从 dummy 走到第 n 个节点
        left 还在 dummy
        
        Step 2：一起走直到 right 到末尾
        right 需要再走 L - n 步到达最后一个节点
        left 也走 L - n 步
        
        right 停在最后一个节点（倒数第1个）,两指针距离 n
        right 在倒数第 1 个
        left 在倒数第 1+n 个 = 倒数第 n+1 个
        T: O（链表长度)
        S: O(1)
        """
        dummy = ListNode(next=head)
        right = dummy
        for _ in range(n):
            right = right.next
        
        left = dummy
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next
        
# @lc code=end

