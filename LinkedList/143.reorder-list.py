#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        revers second half and merge first and second alternately. o(n) o(1)

        Steps:
        1. Find the middle node using slow/fast pointers
        2. Reverse the second half starting from mid
        3. Merge head and reversed second half alternately

        Important:
        - The last node from the reversed list (head2) is shared with the original list.
        - If we continue merging when head2 == last node (e.g., node 3), it might form a self-loop like 3 → 3.
        - So we use `while head2.next:` to skip the last node and avoid a cycle.

        Example:
        Input: [2, 4, 6, 8]
        1: mid = 6
        2: reverse(6) = 8 → 6
        3: merge: 2 → 8 → 4 → 6
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            
            head.next = head2
            head2.next = nxt
            
            # move to the next node
            head = nxt
            head2 = nxt2
            
            
        
# @lc code=end

