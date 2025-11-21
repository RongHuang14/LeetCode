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
if __name__ == "__main__":
    # input: [0, 1, 2, 3, 4, 5, 6]
    # output: [0, n-1, 1, n-2, 2, n-3, ...]
    

